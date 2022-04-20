import { writable, type Writable} from "svelte/store";
import { generateEmptyBoard } from "$src/lib/utils";
import type { Board } from "$src/types";

export const error_message: Writable<string|null> = writable<string|null>(null);
export const info_message: Writable<string|null> = writable<string|null>(null);
export const success_message: Writable<string|null> = writable<string|null>(null);
export const board_is_solution: Writable<boolean|null> = writable<boolean|null>(null);

export const board_state: Writable<Board> = writable<Board>(generateEmptyBoard(4));

export function clearStores(): void {
    error_message.set(null);
    info_message.set(null);
    success_message.set(null);
    board_is_solution.set(null);
}