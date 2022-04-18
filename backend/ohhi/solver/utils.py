from typing import Tuple

import numpy as np

from ohhi.board import Tile

def empty_tile_count(row: np.ndarray) -> int:
    count = 0
    for tile in row:
        if tile == Tile.Empty:
            count += 1
    return count

def check_elems_are_equal(full_row: np.ndarray, other_row: np.ndarray) -> bool:
    for full_elem, other_elem in zip(full_row, other_row):
        if other_elem == Tile.Empty:
            continue
        if other_elem != full_elem:
            return False
    return True

def are_states_different(state1: np.ndarray, state2: np.ndarray) -> bool:
    if state1.shape != state2.shape:
        return True
        #raise ValueError('The input matrices must have the same shape')

    for row1, row2 in zip(state1, state2):
        for elem1, elem2 in zip(row1, row2):
            if elem1 != elem2:
                return True
    return False

def count_tiles(row: np.ndarray) -> Tuple[int, int]:
    yellow_count, blue_count = 0, 0
    for tile in row:
        if tile == Tile.Yellow:
            yellow_count += 1
        elif tile == Tile.Blue: 
            blue_count += 1
    return yellow_count, blue_count

def has_changed_initial_cells(initial_state: np.array, current_state: np.array) -> bool:
    for initial_row, current_row in zip(initial_state, current_state):
        for initial_elem, current_elem in zip(initial_row, current_row):
            if initial_elem != Tile.Empty and initial_elem != current_elem:
                return True
    return False

def get_first_empty_tile(state: np.ndarray, starting_from_row: int=0, starting_from_col: int=0) -> Tuple[int, int]:
    for row_idx, row in enumerate(state[starting_from_row:]):
        if row_idx == starting_from_row:
            for col_idx, tile in enumerate(row[starting_from_col:]):
                if tile == Tile.Empty:
                    return row_idx, col_idx
        else:
            for col_idx, tile in enumerate(row):
                if tile == Tile.Empty:
                    return row_idx, col_idx
    return -1, -1