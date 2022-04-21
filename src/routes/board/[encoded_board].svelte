<script lang="ts">
	import { page } from '$app/stores';

	import { Board as OhhiBoard } from '$lib/ohhi/board';
	import { NoSolutionFound } from '$lib/ohhi/exceptions';
	import { error_message, info_message, board_is_solution, clear_stores } from '$src/stores';

	import PuzzlePageLayout from '$components/layout.svelte';
	import Board from '$components/board.svelte';
	import CopyInput from '$components/copy_input.svelte';
	import Button from '$components/button.svelte';
	import Checkbox from '$components/checkbox.svelte';
	import { Solver } from '$src/lib/ohhi/solver';

	const initial_board_state = OhhiBoard.decode($page.params.encoded_board);
	let board_state = initial_board_state.copy();

	let highlight_initial_board: boolean = false;

	async function find_solution() {
		if (board_state.is_full()) {
			$error_message = null;
			$board_is_solution = null;
			$info_message = 'The board is already full';
			return;
		}

		try {
			board_state = Solver.solve(board_state);
		} catch (err) {
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
			board_state = initial_board_state.copy();
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
	<div slot="left" />

	<div slot="center" class="h-[93vw] w-[93vw]  md:h-[30vw] md:w-[30vw]">
		<Board
			bind:board_state
			can_edit_initial_state={false}
			initial_state={initial_board_state}
			highlight_original={highlight_initial_board}
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
					board_state = initial_board_state.copy();
				}}
				content="clear"
				color="bg-red-500"
			/>
		</div>
		<div class="mt-10 flex items-center gap-3">
			<Checkbox bind:checked={highlight_initial_board} />
			<p class="text-lg font-semibold">highlight initial board state</p>
		</div>
		<div class="mt-16 flex flex-col items-center md:items-start gap-2">
			<h3 class="font-semibold text-xl">share this puzzle:</h3>
			<CopyInput content={`${$page.url.host}/board/${board_state.encode()}`} />
		</div>
	</div>
</PuzzlePageLayout>
