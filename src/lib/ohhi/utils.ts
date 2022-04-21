import { Tile } from './tile';
import { IllegalArgumentException } from './exceptions';

export function count_non_empty_tiles(row: Tile[]): { yellow_count: number; blue_count: number } {
	const res = {
		yellow_count: 0,
		blue_count: 0
	};
	for (const tile of row) {
		if (tile == Tile.Blue) res.blue_count++;
		if (tile == Tile.Yellow) res.yellow_count++;
	}
	return res;
}

export function non_empty_elems_are_equal(row: Tile[], full_row: Tile[]): boolean {
	if (row.length != full_row.length) throw new IllegalArgumentException('Different sizes');
	for (let i = 0; i < row.length; i++) {
		if (row[i] == Tile.Empty) continue;
		if (row[i] !== full_row[i]) return false;
	}
	return true;
}

export function count_empty_tiles(row: Tile[]): number {
	let count = 0;
	for (const tile of row) {
		if (tile == Tile.Empty) count++;
	}
	return count;
}