<script lang="ts">
	import { page } from '$app/stores';

	import { Board as OhhiBoard } from '$lib/ohhi/board';
	import { NoSolutionFound } from '$lib/ohhi/exceptions';
	import { error_message, info_message, success_message, board_is_solution } from '$src/stores';

	import PuzzlePageLayout from '$components/layout.svelte';
	import Board from '$components/board.svelte';
	import CopyInput from '$components/copy_input.svelte';
	import Button from '$components/button.svelte';
	import Checkbox from '$components/checkbox.svelte';
	import { Solver } from '$src/lib/ohhi/solver';

	let encoded_board = $page.params.encoded_board;
	const initial_board_state = OhhiBoard.decode(encoded_board);
	let board_state = initial_board_state.copy();

	const base_website_url = $page.url.host;
	let highlight_initial_board: boolean = false;

	async function findSolutionHandler() {
		try {
			board_state = Solver.solve(board_state);
		} catch (err) {
			if (err instanceof NoSolutionFound) {
				$info_message = null;
				$success_message = null;
				$board_is_solution = null;
				$error_message = 'No solution found for this board';
				return;
			}
			$info_message = null;
			$success_message = null;
			$board_is_solution = null;
			$error_message = 'Something went wrong. Please try again.';
		}
	}

	async function checkSolutionHandler() {
		if (!board_state.is_full()) {
			$error_message = null;
			$success_message = null;
			$board_is_solution = null;
			$info_message = 'Please fill the board before checking the solution.';
			return;
		}
		$board_is_solution = board_state.is_solution();
	}
</script>

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
					$error_message = null;
					checkSolutionHandler();
				}}
				content="check"
				color="bg-green-500"
			/>
			<Button
				click_handler={() => {
					$error_message = null;
					$info_message = null;
					findSolutionHandler();
				}}
				content="solve"
				color="bg-blue-500"
			/>
			<Button
				click_handler={() => {
					$error_message = null;
					$info_message = null;
					$success_message = null;
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
		<div class="mt-16 flex flex-col gap-2">
			<h3 class="font-semibold text-xl">share this puzzle:</h3>
			<CopyInput content={`${base_website_url}/board/${board_state.encode()}`} />
		</div>
	</div>
</PuzzlePageLayout>
