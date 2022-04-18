import enum
from typing_extensions import Self

import rich
import numpy as np

from ohhi.board.utils import rows_are_equal
class Tile(enum.Enum):
    Empty = 1
    Blue = 2
    Yellow = 3

class Board:
    def __init__(self, initial_state: np.array):
        self.size: int = initial_state.shape[0]
        if len(initial_state.shape) != 2 or initial_state.shape[1] != self.size or self.size % 2 != 0:
            raise ValueError("Size must be an even number > 0")
        self.state: np.ndarray = initial_state

    def is_solution(self) -> bool:
        return Board.are_rows_valid(self.state) and Board.are_rows_valid(self.state.T)

    #TODO rename to check_rows
    @staticmethod
    def are_rows_valid(state: np.ndarray, debug: bool = False) -> bool:
        if debug:
            print("------------------\nChecking: ")
            Board(state).pretty_print()
        for row in state:
            blues = 0
            yellows = 0
            consecutive_blues = 0
            consecutive_yellows = 0
            for elem in row:
                # check no gray
                if elem == Tile.Empty:
                    if debug:
                        print("Discarding current solution because it contains an empty tiles.")
                    return False
                elif elem == Tile.Blue:
                    blues += 1
                    consecutive_yellows = 0
                    consecutive_blues +=1
                elif elem == Tile.Yellow:
                    yellows += 1
                    consecutive_blues = 0
                    consecutive_yellows += 1
                
                # check no triplets
                if consecutive_yellows == 3 or consecutive_blues == 3:
                    if debug:
                        print("Discarding current solution because it contains 3 consecutive yellow/blue tiles.")
                    return False

            # check equal number of cells
            if yellows != blues:
                if debug:
                    print("Discarding current solution because one of its rows/columns contains #yellow != #blue.")
                return False

        # check no repeated rows
        for i, row1 in enumerate(state):
            for j, row2 in enumerate(state):
                if i != j and rows_are_equal(row1, row2):
                    if debug:
                        print("Discarding current solution because it contains two copies of the same row/column.")
                    return False
        
        return True

    #Takes a string like "x x x x | y x x y | x b x y | b x x x" and returns the corrisponding board representation
    @staticmethod
    def parse_string(input_string: str) -> Self:
        matrix = []
        for row in input_string.split('|'):
            elems = [elem.strip() for elem in row.strip().split(" ")]
            row = []
            for tile in elems:
                if tile == 'b':
                    row.append(Tile.Blue)
                elif tile == 'y':
                    row.append(Tile.Yellow)
                elif tile == 'x':
                    row.append(Tile.Empty)
                else:
                    raise ValueError(f'Input string malformed. Character "{tile}" not valid')
            matrix.append(row)

        state = np.array(matrix)
        if len(state.shape) != 2 or state.shape[0] != state.shape[1]:
            raise ValueError("Input string not valid. Board sizes mismatch")

        return Board(state)

    def encode(self) -> str:
        rows = []
        for row in self.state:
            current_row  = []
            for tile in row:
                if tile == Tile.Yellow:
                    current_row.append("y")
                elif tile == Tile.Blue:
                    current_row.append("b")
                elif tile == Tile.Empty:
                    current_row.append("x")
            rows.append(" ".join(current_row))
        return " | ".join(rows)


    def pretty_print(self) -> None:
        """ representation: str = ""
        for row in self.state:
            for cell in row:
                if cell == Tile.Empty:
                    representation += ":black_large_square:"
                elif cell == Tile.Blue: 
                    representation += ":blue_square:"
                elif cell == Tile.Yellow:
                    representation += ":yellow_square:"
            representation += "\n"
        rich.print(representation) """
        print(self)

    def __repr__(self) -> str:
        representation: str = ""
        for row in self.state:
            representation = representation + "[" 
            for cell in row[:-1]:
                if cell == Tile.Empty:
                        representation += "   |"
                elif cell == Tile.Blue:
                        representation += " B |"
                elif cell == Tile.Yellow:
                        representation += " Y |"

                #! py >= 3.10
                #match cell: 
                #    case Tile.Empty:
                #        representation += "   |"
                #    case Tile.Blue:
                #        representation += " B |"
                #    case Tile.Yellow:
                #        representation += " Y |"
                       
            if row[-1] == Tile.Empty:
                    representation += "   ]\n"
            elif row[-1] == Tile.Blue:
                    representation += " B ]\n"
            elif row[-1] == Tile.Yellow:
                    representation += " Y ]\n" 
           
            #match row[-1]:
            #    case Tile.Empty:
            #        representation += "   ]\n"
            #    case Tile.Blue:
            #        representation += " B ]\n"
            #    case Tile.Yellow:
            #        representation += " Y ]\n"
        return representation