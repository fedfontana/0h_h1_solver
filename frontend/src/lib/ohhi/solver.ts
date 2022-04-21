import Board, { IllegalArgumentException, NoSolutionFound, Tile } from "./board";

export class Solver {
    static solve(board: Board): Board {
        let old_board = Board.empty_of_size(2);
        let new_board = board.copy();

        while(!new_board.equals(old_board) && !new_board.is_solution()) {
            old_board = new_board.copy();
            new_board = Solver.fill_doubles_sides(new_board);
            new_board = Solver.fill_doubles_sides(new_board.transpose()).transpose();
            new_board = Solver.fill_middle_tiles(new_board);
            new_board = Solver.fill_middle_tiles(new_board.transpose()).transpose();
            new_board = Solver.fill_uneven_rows(new_board);
            new_board = Solver.fill_uneven_rows(new_board.transpose()).transpose();
            new_board = Solver.fill_different_rows(new_board);
            new_board = Solver.fill_different_rows(new_board.transpose()).transpose();
        }

        if(!new_board.is_solution())
            throw new NoSolutionFound('No solution found');
        return new_board;
    }

    static fill_doubles_sides(board: Board): Board {
        const new_board = board.copy();
        for(let row_idx = 0; row_idx < new_board.size; row_idx++) {
            let first_yellow_idx = -1;
            let first_blue_idx = -1;
            let yellow_count = 0;
            let blue_count = 0;
            for(let col_idx = 0; col_idx < new_board.size; col_idx++) {
                switch(new_board.at(row_idx, col_idx)) {
                    case Tile.Yellow:
                        if(yellow_count == 0 || col_idx == 0) {
                            first_blue_idx = -1;
                            first_yellow_idx = col_idx;
                        }
                        blue_count = 0;
                        yellow_count++

                        if(yellow_count == 2) {
                            if(first_yellow_idx > 0 && first_yellow_idx < new_board.size)
                                new_board.state[row_idx][col_idx-1] = Tile.Blue; 
                            if(first_yellow_idx+2 > 0 && first_yellow_idx+2 < new_board.size)
                                new_board.state[row_idx][col_idx+2] = Tile.Blue; 
                        }
                        break;
                    case Tile.Blue:
                        if(blue_count == 0 || col_idx == 0) {
                            first_yellow_idx = -1;
                            first_blue_idx = col_idx;
                        }
                        yellow_count = 0;
                        blue_count++

                        if(blue_count == 2) {
                            if(first_blue_idx > 0 && first_blue_idx < new_board.size)
                                new_board.state[row_idx][col_idx-1] = Tile.Yellow; 
                            if(first_blue_idx+2 > 0 && first_blue_idx+2 < new_board.size)
                                new_board.state[row_idx][col_idx+2] = Tile.Yellow; 
                        }
                        break;
                    case Tile.Empty:
                        first_yellow_idx = -1;
                        first_blue_idx = -1;
                        yellow_count = 0;
                        blue_count = 0;
                }
            }
        }
        return new_board;
    }
    static fill_middle_tiles(board: Board): Board {
        const new_board = board.copy();
        for(let row_idx = 0; row_idx < new_board.size; row_idx++) {
            for(let col_idx = 0; col_idx < new_board.size-2; col_idx++) {
                if(new_board.at(row_idx, col_idx) == Tile.Yellow && new_board.at(row_idx, col_idx+2) == Tile.Yellow)
                    new_board.state[row_idx][col_idx] = Tile.Blue;
                else if(new_board.at(row_idx, col_idx) == Tile.Blue && new_board.at(row_idx, col_idx+2) == Tile.Blue)
                    new_board.state[row_idx][col_idx] = Tile.Yellow;
            }
        }
        return new_board;
    }
    static fill_uneven_rows(board: Board): Board {
        const new_board = board.copy();
        for(let row_idx = 0; row_idx < new_board.size; row_idx++) {
            const {yellow_count, blue_count} = count_non_empty_tiles(new_board[row_idx]);
            if(yellow_count == new_board.size/2) {
                for(let col_idx = 0; col_idx < new_board.size; col_idx++){
                    if(new_board[row_idx][col_idx] == Tile.Empty)
                        new_board[row_idx][col_idx] = Tile.Blue;
                }
            }
            else if(blue_count == new_board.size/2) {
                for(let col_idx = 0; col_idx < new_board.size; col_idx++){
                    if(new_board[row_idx][col_idx] == Tile.Empty)
                        new_board[row_idx][col_idx] = Tile.Yellow;
                }
            }
        }
        return new_board;
    }
    static fill_different_rows(board: Board): Board {
        const new_board = board.copy();
        for(let row1_idx = 0; row1_idx < new_board.size; row1_idx++) {
            if(count_empty_tiles(new_board.state[row1_idx]) != 2)
                continue
            
            for(let row2_idx = 0; row2_idx < new_board.size; row2_idx++) {
                if(row1_idx == row1_idx || count_empty_tiles(new_board.state[row2_idx]) != 0)
                    continue
                if(!non_empty_elems_are_equal(new_board[row1_idx], new_board[row2_idx]))
                    continue
                for(let col_idx = 0; col_idx < new_board.size; col_idx++) {
                    if(new_board[row1_idx][col_idx] != Tile.Empty)
                        continue;
                    if(new_board[row2_idx][col_idx] == Tile.Blue)
                        new_board[row1_idx][col_idx] = Tile.Yellow;
                    else if(new_board[row2_idx][col_idx] == Tile.Yellow)
                        new_board[row1_idx][col_idx] = Tile.Blue;
                }
            }
        }
        return new_board;
    }
}

function count_non_empty_tiles(row: Tile[]): {yellow_count: number, blue_count: number} {
    const res = {
        yellow_count: 0,
        blue_count: 0,
    };
    for(const tile of row) {
        if(tile == Tile.Blue)
            res.blue_count++
        if(tile == Tile.Yellow)
            res.yellow_count++
    }
    return res;
}

function non_empty_elems_are_equal(row: Tile[], full_row: Tile[]): boolean {
    if(row.length != full_row.length)
        throw new IllegalArgumentException('Different sizes');
    for(let i = 0; i < row.length; i++) {
        if(row[i] == Tile.Empty)
            continue;
        if(row[i] !== full_row[i])
            return false;
    }
    return true;
}

function count_empty_tiles(row: Tile[]): number {
    let count = 0;
    for(const tile of row) {
        if(tile == Tile.Empty)
            count++;
    }
    return count;
}