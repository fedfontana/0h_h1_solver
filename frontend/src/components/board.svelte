<script>
	import {generateEmptyBoard} from '../lib/utils';
	export let board_state = generateEmptyBoard(4);

    function clickHandler(row_idx, col_idx, isRightClick) {
        if(board_state[row_idx][col_idx] == "y") {
            board_state[row_idx][col_idx] = isRightClick ? "x" : "b";
        } else if(board_state[row_idx][col_idx] == "b") {
            board_state[row_idx][col_idx] = isRightClick ? "y" : "x";
        } else if(board_state[row_idx][col_idx] == "x") {
            board_state[row_idx][col_idx] = isRightClick ? "b" : "y";
        }
    }
</script>

<div class="flex flex-col gap-4">
	{#each board_state as row, row_idx}
		<div class="flex flex-row gap-4">
			{#each row as tile, col_idx}
				<div
					class={`${
						tile == 'y' ? 'bg-yellow-500' : tile == 'b' ? 'bg-blue-500' : 'bg-neutral-700'
					} w-32 h-32 flex items-center justify-center rounded-xl shadow-lg text-xl font-bold uppercase hover:opacity-80 hover:scale-[98%]
					transition-colors duration-200`}
				    on:click={() => clickHandler(row_idx, col_idx, false)}
                    on:contextmenu|preventDefault={() => clickHandler(row_idx, col_idx, true)}
                />
			{/each}
		</div>
	{/each}
</div>
