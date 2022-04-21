import { IllegalArgumentException } from "./exceptions";

export enum Tile {
    Empty = 1,
    Blue,
    Yellow,
}

export function tile_to_string(tile: Tile): string {
    switch(tile) {
        case Tile.Empty:
            return 'x';
        case Tile.Blue:
            return 'b';
        case Tile.Yellow:
            return 'y';
    }
}

export function string_to_tile(encoded_tile: string): Tile {
    switch(encoded_tile) {
        case 'x':
            return Tile.Empty;
        case 'b':
            return Tile.Blue;
        case 'y':
            return Tile.Yellow;
        default:
            throw new IllegalArgumentException('String representation does not corrispond to any tile.');
    }
}