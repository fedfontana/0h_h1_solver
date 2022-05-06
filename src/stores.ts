import { get, writable, type Writable} from "svelte/store";

export const error_message: Writable<string|null> = writable<string|null>(null);
export const info_message: Writable<string|null> = writable<string|null>(null);
export const board_is_solution: Writable<boolean|null> = writable<boolean|null>(null);
export const theme: Writable<'dark'|'light'> = writable('light');

export function clear_stores(): void {
    error_message.set(null);
    info_message.set(null);
    board_is_solution.set(null);
}

export function initTheme() {
    let local_theme_value: string | null = localStorage.getItem('theme');
    console.log(`Got theme ${local_theme_value} from localstorage`)
    if(local_theme_value !== 'light' && local_theme_value !== 'dark') {
        if(window.matchMedia('(prefers-color-scheme: dark)').matches) {
            local_theme_value = 'dark';
        } else {
            local_theme_value = 'light';
        }
        console.log(`Setting localstorage theme to ${local_theme_value}`);
        localStorage.setItem('theme', local_theme_value);
    }
    theme.set(local_theme_value as 'dark'|'light');
}

export function toggleTheme() {
    if(get(theme) == 'light') {
        theme.set('dark');
    } else {
        theme.set('light');
    }
    localStorage.setItem('theme', get(theme));
}