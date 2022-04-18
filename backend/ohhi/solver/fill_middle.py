import numpy as np

from ohhi.board import Board, Tile
from ohhi.solver import Solver
from ohhi.solver.utils import are_states_different
from ohhi.solver.bruteforce import BruteForceSolver
from ohhi.solver.no_triplets import NoTripletsSolver

class FillMiddleSolver(Solver):
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
            print(f"Alla fine di una iterazione new_state e'\n{Board(new_state)}")
        
        if Board(new_state).is_solution():
            return Board(new_state)
        
        return BruteForceSolver.solve(Board(new_state))

    @staticmethod
    def fill_middle_tiles(state: np.ndarray) -> np.ndarray:
        for row in state: 
            for idx, elem in enumerate(row[:-2]):
                if elem == Tile.Yellow:
                    if row[idx+2] == Tile.Yellow:
                        row[idx+1] = Tile.Blue
                elif elem == Tile.Blue:
                    if row[idx+2] == Tile.Blue:
                        row[idx+1] = Tile.Yellow
        return state