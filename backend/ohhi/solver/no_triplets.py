import numpy as np

from ohhi.board import Board, Tile
from ohhi.solver import Solver
from ohhi.solver.utils import are_states_different
from ohhi.solver.bruteforce import BruteForceSolver
class NoTripletsSolver(Solver):
    @staticmethod
    def solve(initial_state: Board) -> Board:
        old_state = np.array([])
        new_state = initial_state.state
        

        while are_states_different(old_state, new_state) and not Board(new_state).is_solution():
            old_state = new_state.copy()
            new_state = NoTripletsSolver.fill_triplets_sides(new_state)
            new_state = NoTripletsSolver.fill_triplets_sides(new_state.T).T
        
        if Board(new_state).is_solution():
            return Board(new_state)
        

        return BruteForceSolver.solve(Board(new_state))

    @staticmethod
    def fill_triplets_sides(state: np.ndarray) -> np.ndarray:
        for row in state:
            first_yellow_idx = -1
            first_blue_idx = -1
            yellow_count = 0
            blue_count = 0
            for idx, tile in enumerate(row): #check each element
                if tile == Tile.Yellow:
                    #print(f"Checking tile number {idx+1}. blue_count:{blue_count}, yellow_count:{yellow_count}, first_yellow_idx:{first_yellow_idx}")
                    if yellow_count == 0 or idx == 0: #if this is the first yellow tile found in this row/after the last blue/empty tile, update first_yellow_idx
                        first_yellow_idx = idx
                        first_blue_idx = -1
                        #print("Set first yellow idx to", idx)
                    
                    blue_count = 0 
                    yellow_count += 1
                    
                    if yellow_count == 2:
                        #print(f"Found yellows on row {row} from index {first_yellow_idx} to index {first_yellow_idx+2}")
                        if first_yellow_idx > 0 and first_yellow_idx < state.shape[0]: # the second check is useless, of course if there are 2 yellow tiles, the one before the first one is located before the end of the board
                            #print(f"Filling the tile at index {first_yellow_idx-1} (the one before the 2 yellows) with a blue tile.")
                            row[first_yellow_idx-1] = Tile.Blue

                        if first_yellow_idx + 2 > 0 and first_yellow_idx + 2 < state.shape[0]:
                            #print(f"Filling the tile at index {first_yellow_idx+2} (the one after the 2 yellows) with a blue tile.")
                            row[first_yellow_idx+2] = Tile.Blue
                
                elif tile == Tile.Blue:
                    if blue_count == 0 or idx == 0:
                        first_blue_idx = idx
                        first_yellow_idx = -1
                    
                    yellow_count = 0 
                    blue_count += 1
                    
                    if blue_count == 2:
                        if first_blue_idx > 0 and first_blue_idx < state.shape[0]:
                            row[first_blue_idx-1] = Tile.Yellow
                        if first_blue_idx + 2 > 0 and first_blue_idx + 2 < state.shape[0]:
                            row[first_blue_idx+2] = Tile.Yellow
                
                elif tile == Tile.Empty: # when an empty cell is found, reset all of the counter variables
                    first_yellow_idx = -1
                    first_blue_idx = -1
                    yellow_count = 0
                    blue_count = 0
        return state
                        
#TODO nel typing correggere np.array in np.ndarray

#TODO prima fare tutti i vari solver e metterli sequenziali uno dopo l'altro, poi provare mettendoli tutti in un while insieme (?) e poi unire direttamente 
#TODO le funzioni per vedere se cambia qualcosa (meno iterazioni per il check su tutta la matrice --> meno tempo exec)

#TODO scrivere anche una implementazione che fa le cose che deve fare, poi quando non riesce piu' ad andare avanti fa 1 solo giro di brute force e prova con 
#TODO la stessa tattica iniziale a completare tutta la board 