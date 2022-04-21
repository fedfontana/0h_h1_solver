<script lang="ts">
	import { page } from '$app/stores';

	import type { BoardSize } from '$src/types';

	import { SIZES } from '$src/constants';
	import { error_message, info_message, board_is_solution, clear_stores } from '$src/stores';

	import { Board as OhhiBoard } from '$lib/ohhi/board';
	import { NoSolutionFound } from '$lib/ohhi/exceptions';

	import PuzzlePageLayout from '$components/layout.svelte';
	import Board from '$components/board.svelte';
	import Checkbox from '$components/checkbox.svelte';
	import CopyInput from '$components/copy_input.svelte';
	import Button from '$components/button.svelte';
	import { Solver } from '$lib/ohhi/solver';

	let selected_size: BoardSize = 4;

	let board_state = OhhiBoard.empty_of_size(selected_size);

	let pre_solution_board: OhhiBoard | null = null;
	let highlight_initial_board: boolean = false;

	async function find_solution() {
		if (board_state.is_full()) {
			$error_message = null;
			$board_is_solution = null;
			$info_message = 'The board is already full';
			return;
		}

		try {
			pre_solution_board = board_state.copy();
			board_state = Solver.solve(board_state);
		} catch (err) {
			pre_solution_board = null;
			if (err instanceof NoSolutionFound) {
				$info_message = null;
				$board_is_solution = null;
				$error_message = 'No solution found for this board';
				return;
			}
			$info_message = null;
			$board_is_solution = null;
			$error_message = 'Something went wrong. Please try again.';
		}
	}

	async function check_solution() {
		if (!board_state.is_full()) {
			$error_message = null;
			$board_is_solution = null;
			$info_message = 'Please fill the board before checking the solution.';
			return;
		}
		$board_is_solution = board_state.is_solution();
	}

	function shortcuts_handler(e: KeyboardEvent): void {
		if (e.ctrlKey && e.shiftKey && e.key.toLowerCase() === 'l') {
			clear_stores();
			pre_solution_board = null;
			highlight_initial_board = false;
			board_state = OhhiBoard.empty_of_size(selected_size);
		} else if (e.ctrlKey && !e.shiftKey && e.key.toLowerCase() === 'enter') {
			clear_stores();
			check_solution();
		} else if (e.ctrlKey && e.shiftKey && e.key.toLowerCase() === 'enter') {
			clear_stores();
			find_solution();
		} else if (e.key.toLowerCase() === 'escape') {
			clear_stores();
		}
	}
</script>

<svelte:body on:keydown={shortcuts_handler} />

<PuzzlePageLayout>
	<div
		slot="left"
		class="flex flex-row md:flex-col flex-wrap justify-center md:flex-nowrap px-5 md:p-0"
	>
		{#each SIZES as size}
			<button
				class={`m-2 hover:opacity-50 hover:bg-neutral-300 ${
					selected_size == size ? 'bg-neutral-300 bg-opacity-70' : ''
				} px-3 py-1 md:p-1 max-h-20 rounded-lg`}
				on:click={() => {
					highlight_initial_board = false;
					pre_solution_board = null;
					selected_size = size;
					board_state = OhhiBoard.empty_of_size(size);
					clear_stores();
				}}
			>
				<p class="text-3xl md:text-4xl font-semibold">
					{size}x{size}
				</p>
			</button>
		{/each}
	</div>

	<div slot="center" class="h-[93vw] w-[93vw] md:h-[30vw] md:w-[30vw]">
		<Board
			bind:board_state
			initial_state={pre_solution_board}
			highlight_original={highlight_initial_board && pre_solution_board !== null}
		/>
	</div>

	<div slot="right">
		<div class="flex flex-row md:flex-col gap-4">
			<Button
				click_handler={() => {
					clear_stores();
					check_solution();
				}}
				content="check"
				color="bg-green-500"
			/>
			<Button
				click_handler={() => {
					clear_stores();
					find_solution();
				}}
				content="solve"
				color="bg-blue-500"
			/>
			<Button
				click_handler={() => {
					clear_stores();
					pre_solution_board = null;
					highlight_initial_board = false;
					board_state = OhhiBoard.empty_of_size(selected_size);
				}}
				content="clear"
				color="bg-red-500"
			/>
		</div>
		<div class="mt-10 flex items-center gap-3">
			<Checkbox bind:checked={highlight_initial_board} disabled={pre_solution_board === null} />
			<p class={`text-lg font-semibold ${pre_solution_board === null ? 'opacity-60' : ''}`}>
				highlight initial board state
			</p>
		</div>
		<div class="mt-16 flex flex-col gap-2">
			<h3 class="font-semibold text-xl">share this puzzle:</h3>
			<CopyInput content={`${$page.url.host}/board/${board_state.encode()}`} />
		</div>
	</div>
</PuzzlePageLayout>
