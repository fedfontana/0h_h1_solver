export function encodeBoardState(board_state) {
    return board_state.map((row) => row.join('')).join('-');
}

export function decodeBoardState(encoding) {
    return encoding.split('-').map((encoded_row) => encoded_row.split(''));
}

export function generateEmptyBoard(size) {
    let tmp = [];
    for (let i = 0; i < size; i++) {
        let row = [];
        for (let j = 0; j < size; j++) row.push('x');
        tmp.push(row);
    }
    return tmp;
}