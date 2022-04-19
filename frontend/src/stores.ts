import { writable, type Writable} from "svelte/store";
import { generateEmptyBoard } from "$src/lib/utils";
import type { Board } from "$src/types";

export const error_message: Writable<string|null> = writable<string|null>(null);
export const info_message: Writable<string|null> = writable<string|null>(null);
export const success_message: Writable<string|null> = writable<string|null>(null);
export const board_state: Writable<Board> = writable<Board>(generateEmptyBoard(4));