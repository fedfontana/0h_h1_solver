<script lang="ts">
	import { createEventDispatcher } from 'svelte';

    import { page } from '$app/stores';
	import { onDestroy } from 'svelte';

	import type {
		Board as BoardType,
		SolutionResponse,
		ErrorResponse,
		CheckSolutionResponse
	} from '$src/types';

    import { API_URL} from '$src/constants';
	import {
		board_state,
		board_is_solution
	} from '$src/stores';
	import { encodeBoardState, decodeBoardState, generateEmptyBoard, copyBoard} from '$src/lib/utils';

	import PuzzlePageLayout from '$components/layout.svelte';
    import Board from '$components/board.svelte';
	import CopyInput from '$components/copy_input.svelte';
	import Button from '$components/button.svelte';
	import Checkbox from '$components/checkbox.svelte';

	let encoded_board = $page.params.encoded_board;
	const initial_board_state = decodeBoardState(encoded_board);
	$board_state = copyBoard(initial_board_state); 

	const dispatch = createEventDispatcher();

	const base_website_url = $page.url.host;
	let highlight_initial_board: boolean = false;


	async function findSolutionHandler() {
		let response = await fetch(`${API_URL}/get_solution/${encodeBoardState($board_state)}`);
		let status = response.status;
		let JSONRes: SolutionResponse | ErrorResponse = await response.json();
		if (status == 404) {
			// no solution found
			$board_is_solution = null;
			dispatch('error_', {
				message: (JSONRes as ErrorResponse).error_message,
			})
			return;
		}
		if (!response.ok) {
			// catch all of the unhandled errors
			$board_is_solution = null;
			dispatch('error_', {
				message: 'Something went wrong. Please try again.',
			})
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
			dispatch('info', {
				message: 'Please fill the board before checking the solution.',
			})
			return;
		}
		let response = await fetch(`${API_URL}/check_solution/${encodeBoardState($board_state)}`);
		let JSONRes: CheckSolutionResponse | ErrorResponse = await response.json();
		if (!response.ok) {
			// catch all of the unhandled errors
			$board_is_solution = null;
			dispatch('error_', {
				message: 'Something went wrong. Please try again.',
			})
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
		<Board bind:board_state={$board_state} can_edit_initial_state={false} initial_state={initial_board_state} highlight_original={highlight_initial_board}/>
	</div>

	<div slot="right">
		<div class="flex flex-row md:flex-col gap-4">
			<Button
				click_handler={checkSolutionHandler}
				content="check"
				color="bg-green-500"
			/>
			<Button
				click_handler={findSolutionHandler}
				content="solve"
				color="bg-blue-500"
			/>
			<Button
				click_handler={() => {
					$board_state = copyBoard(initial_board_state);
				}}
				content="clear"
				color="bg-red-500"
			/>
		</div>
		<div class="mt-10 flex items-center gap-3">
			<Checkbox bind:checked={highlight_initial_board}/> 
			<p class="text-lg font-semibold">highlight initial board state</p>
		</div>
		<div class="mt-16 flex flex-col gap-2">
			<h3 class="font-semibold text-xl">share this puzzle:</h3>
			<CopyInput content={`${base_website_url}/board/${encodeBoardState($board_state)}`} />
		</div>
	</div>
</PuzzlePageLayout>
