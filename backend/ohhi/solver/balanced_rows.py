import numpy as np

from ohhi.board import Board, Tile
from ohhi.solver import Solver
from ohhi.solver.utils import count_tiles, are_states_different
from ohhi.solver.bruteforce import BruteForceSolver
from ohhi.solver.no_triplets import NoTripletsSolver
from ohhi.solver.fill_middle import FillMiddleSolver

class CheckBalancedRowsSolver(Solver):
    
    @staticmethod
    def solve(initial_state: Board) -> Board:
        old_state = np.array([])
        new_state = initial_state.state

        while are_states_different(old_state, new_state) and not Board(new_state).is_solution():
            old_state = new_state.copy()
            new_state = NoTripletsSolver.fill_triplets_sides(new_state)
            new_state = NoTripletsSolver.fill_triplets_sides(new_state.T).T
            new_state = FillMiddleSolver.fill_middle_tiles(new_state)
            new_state = FillMiddleSolver.fill_middle_tiles(new_state.T).T
            new_state = CheckBalancedRowsSolver.fill_uneven_rows(new_state)
            new_state = CheckBalancedRowsSolver.fill_uneven_rows(new_state.T).T
        
        if Board(new_state).is_solution():
            return Board(new_state)
        
        return BruteForceSolver.solve(Board(new_state))

    @staticmethod
    def fill_uneven_rows(state: np.ndarray) -> np.ndarray:
        for row in state:
            yellow_count, blue_count = count_tiles(row)
            if yellow_count == state.shape[0]/2:
                for idx, tile in enumerate(row):
                    if tile == Tile.Empty:
                        #print(f'Filling tile at index {idx} in row {row} with blue')
                        row[idx] = Tile.Blue
            elif blue_count == state.shape[0]/2:
                for idx, tile in enumerate(row):
                    if tile == Tile.Empty:
                        #print(f'Filling tile at index {idx} in row {row} with yellow')
                        row[idx] = Tile.Yellow
        return state
