import { writable, type Writable} from "svelte/store";

export const error_message: Writable<string|null> = writable<string|null>(null);
export const info_message: Writable<string|null> = writable<string|null>(null);
export const success_message: Writable<string|null> = writable<string|null>(null);
export const board_is_solution: Writable<boolean|null> = writable<boolean|null>(null);