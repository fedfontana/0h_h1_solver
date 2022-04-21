export enum Tile {
    Empty = 1,
    Blue,
    Yellow,
}

export class IllegalArgumentException extends Error {}; 
export class NoSolutionFound extends Error {};

export function tile_to_string(tile: Tile): string {
    switch(tile) {
        case Tile.Empty:
            return 'x';
        case Tile.Blue:
            return 'b';
        case Tile.Yellow:
            return 'y';
    }
}

export function string_to_tile(encoded_tile: string): Tile {
    switch(encoded_tile) {
        case 'x':
            return Tile.Empty;
        case 'b':
            return Tile.Blue;
        case 'y':
            return Tile.Yellow;
        default:
            throw new IllegalArgumentException('String representation does not corrispond to any tile.');
    }
}

export class Board {
    size: number;
    state: Tile[][];
    constructor(initial_state: Tile[][]) {
        this.size = initial_state.length;
        if(initial_state.length % 2 != 0 || initial_state.length <= 0 || initial_state[0].length != initial_state.length)
            throw new IllegalArgumentException('Illegal board size');
        this.state = initial_state;
    }

    static empty_of_size(size: number): Board {
        const arr: Tile[][] = [];
        for(let i = 0; i < size; i++) {
            const row: Tile[] = [];
            for(let j = 0; j < size; j++) {
                row.push(Tile.Empty);
            }
            arr.push(row);
        }
        return new Board(arr);
    }

    encode(): string {
        return this.state.map((row) => row.map(tile => tile_to_string(tile)).join('')).join('-');
    }

    static decode(encoded_board: string): Board {
        return new Board(encoded_board.split('-').map((encoded_row) => encoded_row.split('').map(tile_repr => string_to_tile(tile_repr))));
    }

    copy(): Board {
        return new Board(this.state.map(row => row.slice()));
    }

    private check_rows(): boolean {
        for(const row of this.state) {
            let blues = 0;
            let yellows = 0;
            let consecutive_blues = 0;
            let consecutive_yellows = 0;
            for(const tile of row) {
                switch(tile) {
                    case Tile.Empty:
                        return false;
                    case Tile.Blue:
                        blues++;
                        consecutive_blues++;
                        consecutive_yellows = 0;
                        break;
                    case Tile.Yellow:
                        yellows++;
                        consecutive_yellows++;
                        consecutive_blues = 0;
                        break;
                }
                if(consecutive_blues == 3 || consecutive_yellows == 3)
                    return false;
            }
            if(yellows != blues)
                return false;
        }
        for(let row1_idx = 0; row1_idx < this.size; row1_idx++) {
            for(let row2_idx = 0; row2_idx < this.size; row2_idx++) {
                if(row1_idx != row2_idx && Board.rows_are_equal(this.state[row1_idx], this.state[row2_idx])) {
                    return false;
                }
            }
        }
        return true;
    }

    at(row_idx: number, col_idx: number): Tile|undefined {
        return this.state.at(row_idx)?.at(col_idx);
    }

    transpose(): Board {
        const board_copy = Board.empty_of_size(this.size);
        for(let row_idx = 0; row_idx < board_copy.size; row_idx++) {
            for(let col_idx = 0; col_idx < board_copy.size; col_idx++) {
                board_copy.state[row_idx][col_idx] = (this.at(col_idx, row_idx) as Tile);
            }
        }
        return board_copy;
    }

    is_full(): boolean {
        for(let row_idx = 0; row_idx < this.size; row_idx++) {
            for(let col_idx = 0; col_idx < this.size; col_idx++) {
                if(this.at(row_idx, col_idx) == Tile.Empty) return true;
            }
        }
        return false;
    }


    is_solution(): boolean {
        return this.check_rows() && this.transpose().check_rows();
    }    

    private static rows_are_equal(row1: Tile[], row2: Tile[]): boolean {
        for(let i = 0; i < row1.length; i++) {
            if(row1[i] != row2[i])
                return false;
        }
        return true;
    }

    equals(other: Board): boolean {
        if(this.size != other.size) return false;

        for(let row_idx = 0; row_idx < this.size; row_idx++) {
            for(let col_idx = 0; col_idx < this.size; col_idx++) {
                if(this.at(row_idx, col_idx) != other.at(row_idx, col_idx)) return false;
            }
        }
        return true;
    }
}