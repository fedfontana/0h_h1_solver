export type Tile =  'x' | 'y' | 'b';
export type Board = Tile[][];
export type ToastType = 'error' | 'info' | 'success';
export type BoardSize = 4 | 6 | 8 | 10 | 12;

export type SolutionResponse = { solution: string };
export type ErrorResponse = { error_message: string };
export type CheckSolutionResponse = { is_solution: boolean };