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

	const classes_per_size = {
		"4": "rounded-2xl md:rounded-3xl gap-2 md:gap-5",
		"6": "rounded-xl md:rounded-2xl gap-1 md:gap-4",
		"8": "rounded-[0.63rem] md:rounded-2xl gap-[0.2rem] md:gap-2",
		"10": "rounded-lg md:rounded-xl gap-[0.125rem] md:gap-2",
		"12": "rounded-md md:rounded-xl gap-[0.125rem] md:gap-1"
	}

</script>

<!--? why is the desktop app taking mobile gap sizes? -->

<div class={`flex flex-col h-full w-full justify-between ${classes_per_size[board_state.length]}`}
	on:contextmenu|preventDefault
>
	{#each board_state as row, row_idx}
		<div class={`flex flex-row w-full justify-between flex-1 ${classes_per_size[board_state.length]}`}>
			{#each row as tile, col_idx}
				<div
					class={`${
						tile == 'y' ? 'bg-[#ffd700]' : tile == 'b' ? 'bg-[#0057b7]' : 'bg-neutral-700'
					} flex-1 ${classes_per_size[board_state.length]} shadow-lg hover:opacity-80 hover:scale-[98%]
					transition-colors duration-200`}
				    on:click={() => clickHandler(row_idx, col_idx, false)}
                    on:contextmenu|preventDefault={() => clickHandler(row_idx, col_idx, true)}
                />
			{/each}
		</div>
	{/each}
</div>