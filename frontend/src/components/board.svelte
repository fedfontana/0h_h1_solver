<script lang="ts">
	import {generateEmptyBoard} from '$src/lib/utils';
	export let board_state = generateEmptyBoard(4);

    function clickHandler(row_idx: number, col_idx: number, isRightClick: boolean): void {
        if(board_state[row_idx][col_idx] == "y") {
            board_state[row_idx][col_idx] = isRightClick ? "x" : "b";
        } else if(board_state[row_idx][col_idx] == "b") {
            board_state[row_idx][col_idx] = isRightClick ? "y" : "x";
        } else if(board_state[row_idx][col_idx] == "x") {
            board_state[row_idx][col_idx] = isRightClick ? "b" : "y";
        }
    }

	const gap_sizes = {
		"4": 5,
		"6": 4,
		"8": 2,
		"10": 2,
		"12": 1
	};

	const rounded_size = {
		"4": "3xl",
		"6": "2xl",
		"8": "2xl",
		"10": "xl",
		"12": "xl"
	};
</script>

<div class={`flex flex-col h-full w-full justify-between gap-y-${gap_sizes[board_state.length]}`}>
	{#each board_state as row, row_idx}
		<div class={`flex flex-row w-full justify-between flex-1 gap-x-${gap_sizes[board_state.length]}`}>
			{#each row as tile, col_idx}
				<div
					class={`${
						tile == 'y' ? 'bg-yellow-500' : tile == 'b' ? 'bg-blue-500' : 'bg-neutral-700'
					} flex-1 rounded-${rounded_size[board_state.length]} shadow-lg hover:opacity-80 hover:scale-[98%]
					transition-colors duration-200`}
				    on:click={() => clickHandler(row_idx, col_idx, false)}
                    on:contextmenu|preventDefault={() => clickHandler(row_idx, col_idx, true)}
                />
			{/each}
		</div>
	{/each}
</div>