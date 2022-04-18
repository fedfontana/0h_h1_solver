import itertools
from typing import Iterator

import numpy as np

from ohhi.board import Board, Tile
from ohhi.solver import Solver
from ohhi.solver.utils import get_first_empty_tile, has_changed_initial_cells
from ohhi.solver.exceptions import NoSolutionFound

#TODO check how this behaves if the initial board is already a solution
class BruteForceSolver(Solver):
    @staticmethod
    def solve(initial_state: Board) -> Board:
        for possible_solution in BruteForceSolver.generate_possible_boards(initial_state):
            if possible_solution.is_solution():
                return possible_solution
        raise NoSolutionFound("No solution has been found for this initial board.")

    #TODO check if this produces stuff like
    #two copies "Y B | B Y" (and similar ones) (technically the two yellows/blues get swapped), useless computations? avoidable?

    def generate_possible_boards(initial_state: Board) -> Iterator[Board]:
        count = 0
        for possible_solution in itertools.product([Tile.Blue, Tile.Yellow], repeat=initial_state.size**2):
            new_state = np.reshape(possible_solution, (initial_state.size, initial_state.size))

            # scan the board and skip iteration if the current `new_state` happened to have changed an initial tile
            if has_changed_initial_cells(initial_state.state, new_state):
                continue
            count += 1
            print(count)

            yield Board(new_state)

    @staticmethod
    def tentative_solve(initial_board: Board) -> Board:
        if initial_board.is_solution():
            return initial_board
        
        sol = BruteForceSolver.tentative_rec_solve(initial_board.state, 0, 0)
        if sol is None:
            raise NoSolutionFound('No solution found')
        
        return sol

    @staticmethod
    def tentative_rec_solve(initial_state: np.ndarray, starting_from_row: int, starting_from_col: int) -> Board | None:
        empty_tile_row, empty_tile_col = get_first_empty_tile(initial_state, starting_from_row=starting_from_row, starting_from_col=starting_from_col)
        if (empty_tile_row, empty_tile_col) == (-1, -1):
            if Board(initial_state).is_solution():
                return Board(initial_state)
            return None

        next_cell_row, next_cell_col = empty_tile_row, empty_tile_col + 1
        if next_cell_col > initial_state.shape[0]:
            next_cell_row += 1
            next_cell_col = 0
        if next_cell_row > initial_state.shape[0]:
            return None

        initial_state[empty_tile_row][empty_tile_col] = Tile.Yellow
        copy_sol =  BruteForceSolver.tentative_rec_solve(initial_state, next_cell_row, next_cell_col)
        if copy_sol is not None:
            return copy_sol
        
        initial_state[empty_tile_row][empty_tile_col] = Tile.Blue
        copy_sol =  BruteForceSolver.tentative_rec_solve(initial_state, next_cell_row, next_cell_col)
        if copy_sol is not None:
            return copy_sol
                
        initial_state[empty_tile_row][empty_tile_col] = Tile.Empty
        return None


#TODO add [i,j] notation to the board class

#TODO in future "smarter" solvers, add optional pretty prints detailing how the algorithm is building the solution
#e.g.: "Adding a blue square because of the 3-in-a-row rule:\n{current_board_state}"