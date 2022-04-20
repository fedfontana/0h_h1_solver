<script lang="ts">
    import { page } from '$app/stores';
    import Board from '$components/board.svelte';
	import { onDestroy } from 'svelte';
	import PuzzlePageLayout from '$components/layout.svelte';
	import CopyInput from '$components/copy_input.svelte';
	import Button from '$components/button.svelte';
    import { API_URL, WEBSITE_URL} from '$src/constants';
	import type {
		Board as BoardType,
		SolutionResponse,
		ErrorResponse,
		CheckSolutionResponse
	} from '$src/types';
	import { encodeBoardState, decodeBoardState, generateEmptyBoard } from '$src/lib/utils';
	import {
		board_state,
		error_message,
		info_message,
		success_message,
		board_is_solution
	} from '$src/stores';

    let encoded_board = $page.params.encoded_board;

	const initial_board_state = decodeBoardState(encoded_board);
	$board_state = copyBoard(initial_board_state); 

    function copyBoard(board: BoardType): BoardType {
        return board.map(row => row.slice());
    } 
        
	async function findSolutionHandler() {
		let response = await fetch(`${API_URL}/get_solution/${encodeBoardState($board_state)}`);
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
		$board_state = decodeBoardState((JSONRes as SolutionResponse).solution);
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
		if (!isBoardFull($board_state)) {
			$error_message = null;
			$success_message = null;
			$board_is_solution = null;
			$info_message = 'Please fill the board before checking the solution.';
			return;
		}
		let response = await fetch(`${API_URL}/check_solution/${encodeBoardState($board_state)}`);
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

	onDestroy(() => {
		$board_state = generateEmptyBoard(4);
	});
</script>

<PuzzlePageLayout>
	<div
		slot="left"
	>
	</div>

	<div slot="center" class="h-[93vw] w-[93vw]  md:h-[30vw] md:w-[30vw]">
		<Board bind:board_state={$board_state} />
	</div>

	<div slot="right">
		<div class="flex flex-row md:flex-col gap-4">
			<Button
				clickHandler={() => {
					$error_message = null;
					checkSolutionHandler();
				}}
				content="check"
				color="bg-green-500"
			/>
			<Button
				clickHandler={() => {
					$error_message = null;
					$info_message = null;
					findSolutionHandler();
				}}
				content="solve"
				color="bg-blue-500"
			/>
			<Button
				clickHandler={() => {
					$error_message = null;
					$info_message = null;
					$success_message = null;
					$board_state = copyBoard(initial_board_state);
				}}
				content="clear"
				color="bg-red-500"
			/>
		</div>
		<div class="mt-16 flex flex-col gap-2">
			<h3 class="font-semibold text-xl">share this puzzle:</h3>
			<CopyInput content={`${WEBSITE_URL}/board/${encodeBoardState($board_state)}`} />
		</div>
	</div>
</PuzzlePageLayout>
