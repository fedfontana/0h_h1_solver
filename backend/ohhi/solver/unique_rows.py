import numpy as np

from ohhi.board import Board, Tile
from ohhi.solver import Solver
from ohhi.solver.exceptions import NoSolutionFound
from ohhi.solver.utils import empty_tile_count, check_elems_are_equal, are_states_different
from ohhi.solver.no_triplets import NoTripletsSolver
from ohhi.solver.fill_middle import FillMiddleSolver
from ohhi.solver.balanced_rows import CheckBalancedRowsSolver

class CheckUniqueRowsSolver(Solver):
    
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
            new_state = CheckUniqueRowsSolver.fill_different_rows(new_state)
            new_state = CheckUniqueRowsSolver.fill_different_rows(new_state.T).T
        
        if not Board(new_state).is_solution():
            raise NoSolutionFound('No solution found')
            
        return Board(new_state)

    @staticmethod
    def fill_different_rows(state: np.ndarray) -> np.ndarray:
        for row_idx, row in enumerate(state):
            if empty_tile_count(row) != 2:
                continue
            for other_idx, other_row in enumerate(state):
                if other_idx == row_idx or empty_tile_count(other_row) != 0: # no need to check a row against itself or a row with empty elements
                    continue
                if not check_elems_are_equal(other_row, row): # if the tiles of the full row do not coincide with the non empty elems of the non-full row, this method cannot be applied
                    continue
                for idx, (tile, other_tile) in enumerate(zip(row, other_row)):
                    if tile != Tile.Empty:
                        continue
                    if other_tile == Tile.Blue:
                        row[idx] = Tile.Yellow
                    elif other_tile == Tile.Yellow:
                        row[idx] = Tile.Blue
        return state
