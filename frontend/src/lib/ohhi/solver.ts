import Board, { NoSolutionFound } from "./board";

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
        throw Error();
    }
    static fill_middle_tiles(board: Board): Board {
        throw Error();

    }
    static fill_uneven_rows(board: Board): Board {
        throw Error();
    }
    static fill_different_rows(board: Board): Board {
        throw Error();
    }
}