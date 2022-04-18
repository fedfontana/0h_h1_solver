import numpy as np

def rows_are_equal(row1: np.ndarray, row2: np.ndarray) -> bool:
    return all([elem1 == elem2 for elem1, elem2 in zip(row1, row2)])