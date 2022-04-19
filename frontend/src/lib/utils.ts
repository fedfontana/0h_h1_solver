import type { Tile, Board, BoardSize } from '../types';

export function encodeBoardState(board_state: Board): string {
    return board_state.map((row) => row.join('')).join('-');
}

export function decodeBoardState(encoding: string): Board {
    return encoding.split('-').map((encoded_row) => (encoded_row.split('') as Tile[]));
}

export function generateEmptyBoard(size: BoardSize): Board {
    const tmp: Board = [];
    for (let i = 0; i < size; i++) {
        const row: Tile[] = [];
        for (let j = 0; j < size; j++) row.push('x');
        tmp.push(row);
    }
    return tmp;
}