import { writable } from "svelte/store";
import type { Writable } from "svelte/store";

export const error_message: Writable<string|null> = writable<string|null>(null);