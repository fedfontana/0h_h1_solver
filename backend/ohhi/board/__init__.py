import enum
from typing_extensions import Self

import rich
import numpy as np

from ohhi.board import utils
class Tile(enum.Enum):
    Empty = 1
    Blue = 2
    Yellow = 3

    def to_string(self) -> str:
        if self == Tile.Blue:
            return 'b'
        elif self == Tile.Yellow:
            return 'y'
        elif self == Tile.Empty:
            return 'x'

def string_to_tile(tile: str) -> Self:
        if tile == 'b':
            return Tile.Blue
        elif tile == 'y':
            return Tile.Yellow
        elif tile == 'x':
            return Tile.Empty
        raise ValueError(f'Input string malformed. Character "{tile}" isn\'t a valid tile representation.')

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
                if i != j and utils.rows_are_equal(row1, row2):
                    if debug:
                        print("Discarding current solution because it contains two copies of the same row/column.")
                    return False
        
        return True

    # Parses a string like "x x x x | y x x y | x b x y | b x x x" and returns the corrisponding board representation
    @staticmethod
    def parse_string(input_string: str) -> Self:
        matrix = []
        for row in input_string.split(' | '):
            matrix.append([string_to_tile(token.strip()) for token in row.strip().split(" ")])

        state = np.array(matrix)
        return Board(state)

    # Encoded the current state in a string of type xxby-xbby-xybb-xxxx
    def encode(self) -> str:
        rows = []
        for row in self.state:
            rows.append("".join([tile.to_string() for tile in row]))
        return "-".join(rows)

    # Decodes a string of type xxby-xbby-xybb-xxxx into a Board object
    @staticmethod
    def decode(input_string: str) -> Self:
        matrix = []
        for row in input_string.split('-'):
            matrix.append([string_to_tile(token) for token in row.strip()])

        state = np.array(matrix)
        return Board(state)        


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
            for tile in row[:-1]:
                if tile == Tile.Empty:
                        representation += "   |"
                elif tile == Tile.Blue:
                        representation += " B |"
                elif tile == Tile.Yellow:
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