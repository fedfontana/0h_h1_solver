<script lang="ts">
	import { page } from '$app/stores';
	
	import type {
		Board as BoardType,
		BoardSize,
		SolutionResponse,
		ErrorResponse,
		CheckSolutionResponse
	} from '$src/types';

	import { API_URL, SIZES } from '$src/constants';
	import {
		error_message,
		info_message,
		success_message,
		board_is_solution
	} from '$src/stores';
	import { encodeBoardState, decodeBoardState, generateEmptyBoard, copyBoard } from '$lib/utils';

	import PuzzlePageLayout from '$components/layout.svelte';
	import Board from '$components/board.svelte';
	import Checkbox from '$components/checkbox.svelte';
	import CopyInput from '$components/copy_input.svelte';
	import Button from '$components/button.svelte';

	let base_website_url = $page.url.host;
	let selected_size: BoardSize = 4;

	$error_message = null;
	$info_message = null;
	$success_message = null;
	let board_state = generateEmptyBoard(selected_size);

	let pre_solution_board: BoardType |null = null;
	let highlight_initial_board: boolean = false;

	async function findSolutionHandler() {
		let response = await fetch(`${API_URL}/get_solution/${encodeBoardState(board_state)}`);
		let status = response.status;
		let JSONRes: SolutionResponse | ErrorResponse = await response.json();
		if (status == 404) {
			// no solution found
			$info_message = null;
			$success_message = null;
			$board_is_solution = null;
			$error_message = (JSONRes as ErrorResponse).error_message;
			return;
		}
		if (!response.ok) {
			// catch all of the unhandled errors
			$info_message = null;
			$success_message = null;
			$board_is_solution = null;
			$error_message = 'Something went wrong. Please try again.';
			return;
		}
		pre_solution_board = copyBoard(board_state);
		board_state = decodeBoardState((JSONRes as SolutionResponse).solution);
	}

	function isBoardFull(board_state: BoardType): boolean {
		for (let row of board_state) {
			for (let tile of row) {
				if (tile == 'x') return false;
			}
		}
		return true;
	}

	async function checkSolutionHandler() {
		if (!isBoardFull(board_state)) {
			$error_message = null;
			$success_message = null;
			$board_is_solution = null;
			$info_message = 'Please fill the board before checking the solution.';
			return;
		}
		let response = await fetch(`${API_URL}/check_solution/${encodeBoardState(board_state)}`);
		let JSONRes: CheckSolutionResponse | ErrorResponse = await response.json();
		if (!response.ok) {
			// catch all of the unhandled errors
			$info_message = null;
			$success_message = null;
			$board_is_solution = null;
			$error_message = 'Something went wrong. Please try again.';
			return;
		}
		$board_is_solution = (JSONRes as CheckSolutionResponse).is_solution;
	}
</script>

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
					board_state = generateEmptyBoard(size);
					$error_message = null;
					$info_message = null;
				}}
			>
				<p class="text-3xl md:text-4xl font-semibold">
					{size}x{size}
				</p>
			</button>
		{/each}
	</div>

	<div slot="center" class="h-[93vw] w-[93vw]  md:h-[30vw] md:w-[30vw]">
		<Board bind:board_state={board_state} initial_state={pre_solution_board} highlight_original={highlight_initial_board && pre_solution_board !== null} />
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
					pre_solution_board = null;
					highlight_initial_board = false;
					board_state = generateEmptyBoard(selected_size);
				}}
				content="clear"
				color="bg-red-500"
			/>
		</div>
		<div class="mt-10 flex items-center gap-3">
			<Checkbox bind:checked={highlight_initial_board} disabled={pre_solution_board === null}/> 
			<p class={`text-lg font-semibold ${pre_solution_board === null ? 'opacity-60' : ''}`}>highlight initial board state</p>
		</div>
		<div class="mt-16 flex flex-col gap-2">
			<h3 class="font-semibold text-xl">share this puzzle:</h3>
			<CopyInput content={`${base_website_url}/board/${encodeBoardState(board_state)}`} />
		</div>
	</div>
</PuzzlePageLayout>
