<script lang="ts">
	import Board from '$components/board.svelte';
	import { onDestroy } from 'svelte';
	import { board_state } from '$src/stores';
	import { generateEmptyBoard } from '$src/lib/utils';
	onDestroy(() => {
		$board_state = generateEmptyBoard(4);
	})
</script>

<div class="h-[30vw] w-[30vw]">
	<Board bind:board_state={$board_state} />
</div>
