<script lang="ts">
	import '$src/app.css';
	import CopyInput from '$components/copy_input.svelte';
	import Toast from '$components/toast.svelte';
	import Button from '$components/button.svelte';
	import type {
		Board as BoardType,
		BoardSize,
		SolutionResponse,
		ErrorResponse,
		CheckSolutionResponse
	} from '$src/types';
	import { encodeBoardState, decodeBoardState, generateEmptyBoard } from '$src/lib/utils';
	import { board_state, error_message, info_message, success_message } from '$src/stores';

	const API_URL = 'http://localhost:5000';
	const WEBSITE_URL = 'http://localhost:3000';

	const SIZES: BoardSize[] = [4, 6, 8, 10, 12];
	let selected_size: BoardSize = 4;

	$error_message = null;
	$info_message = null;
	$success_message = null;
	$board_state = generateEmptyBoard(selected_size);

	let is_solution: boolean | null = null;

	async function findSolutionHandler() {
		let response = await fetch(`${API_URL}/get_solution/${encodeBoardState($board_state)}`);
		let status = response.status;
		let JSONRes: SolutionResponse | ErrorResponse = await response.json();
		if (status == 404) {
			// no solution found
			$info_message = null;
			$success_message = null;
			is_solution = null;
			$error_message = (JSONRes as ErrorResponse).error_message;
			return;
		}
		if (!response.ok) {
			// catch all of the unhandled errors
			$info_message = null;
			$success_message = null;
			is_solution = null;
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
			is_solution = null;
			$info_message = 'Please fill the board before checking the solution.';
			return;
		}
		let response = await fetch(`${API_URL}/check_solution/${encodeBoardState($board_state)}`);
		let JSONRes: CheckSolutionResponse | ErrorResponse = await response.json();
		if (!response.ok) {
			// catch all of the unhandled errors
			$info_message = null;
			$success_message = null;
			is_solution = null;
			$error_message = 'Something went wrong. Please try again.';
			return;
		}
		is_solution = (JSONRes as CheckSolutionResponse).is_solution;
	}
</script>

<div class="relative w-full h-full flex flex-col py-12 md:w-8/12 mx-auto">
	<nav class="mb-5 md:mb-0">
		<h1 class="text-5xl md:text-8xl font-bold text-center w-full h-[8%]">
			<a href="/">0h h1 solver</a>
		</h1>
	</nav>
	<div
		class="relative h-[92%] w-full flex flex-col items-center justify-center gap-5 md:gap-12 md:flex-row"
	>
		{#if $error_message != null}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					clickHandler={() => {
						$error_message = null;
						$info_message = null;
					}}
					content={$error_message}
					buttonText="close"
				/>
			</div>
		{/if}
		{#if $info_message != null}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					type="info"
					clickHandler={() => {
						$error_message = null;
						$info_message = null;
					}}
					content={$info_message}
					buttonText="close"
				/>
			</div>
		{/if}
		{#if is_solution == true}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					type="success"
					clickHandler={() => {
						is_solution = null;
						$info_message = null;
						$error_message = null;
					}}
					content="Your solution is correct!"
					buttonText="close"
				/>
			</div>
		{:else if is_solution == false}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					clickHandler={() => {
						is_solution = null;
						$info_message = null;
						$error_message = null;
					}}
					content="Your solution is wrong."
					buttonText="close"
				/>
			</div>
		{/if}

		<!-- LEFT SIDE -->
		<div
			class="flex flex-row md:flex-col flex-[2] flex-wrap mx-auto w-full justify-center md:flex-nowrap px-5 md:p-0"
		>
			{#each SIZES as size}
				<button
					class={`m-2 hover:opacity-50 hover:bg-neutral-300 ${
						selected_size == size ? 'bg-neutral-300 bg-opacity-70' : ''
					} px-3 py-1 md:p-1 max-h-20 rounded-lg`}
					on:click={() => {
						selected_size = size;
						$board_state = generateEmptyBoard(size);
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
		<!--/LEFT SIDE  -->

		<!-- CENTER -->
		<div class="flex flex-col w-full items-center justify-center flex-[4] md:flex-[6]">
			<slot />
		</div>
		<!--/CENTER -->

		<!-- RIGHT SIDE -->
		<div class="flex-[2] mt-5 md:mt-0">
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
						$board_state = generateEmptyBoard(selected_size);
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
		<!--/RIGHT SIDE -->
	</div>
</div>
