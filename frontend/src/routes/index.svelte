<script lang="ts">
	import CopyInput from '../components/copy_input.svelte';
	import Board from '../components/board.svelte';
	import Toast from '../components/toast.svelte';
	import Button from '../components/button.svelte';
	import type {Board as BoardType, BoardSize, SolutionResponse, ErrorResponse, CheckSolutionResponse } from '../types';
	import { encodeBoardState, decodeBoardState, generateEmptyBoard } from '../lib/utils';
	const API_URL = 'http://localhost:5000';
	const WEBSITE_URL = 'http://localhost:3000';

	const SIZES: BoardSize[] = [4, 6, 8, 10, 12];
	let selected_size: BoardSize = 4;

	let error_msg: string|null = null;
	let info_msg: string|null = null;

	let is_solution: boolean|null = null;

	let board_state = generateEmptyBoard(selected_size);

	async function findSolutionHandler() {
		let response = await fetch(`${API_URL}/get_solution/${encodeBoardState(board_state)}`);
		let status = response.status;
		let JSONRes: SolutionResponse | ErrorResponse = await response.json();
		if (status == 404) {
			// no solution found
			error_msg = (JSONRes as ErrorResponse).error_message;
			return;
		}
		if (!response.ok) {
			// catch all of the unhandled errors
			error_msg = 'Something went wrong. Please try again.';
			return;
		}
		board_state = decodeBoardState((JSONRes as SolutionResponse).solution);
	}

	function isBoardFull(board_state: BoardType): boolean {
		for(let row of board_state) {
			for(let tile of row) {
				if(tile == 'x') return false;
			}
		}
		return true;
	}

	async function checkSolutionHandler() {
		if(!isBoardFull(board_state)) {
			info_msg = "Please fill the board before checking the solution.";
			return
		}
		let response= await fetch(`${API_URL}/check_solution/${encodeBoardState(board_state)}`);
		let JSONRes: CheckSolutionResponse|ErrorResponse  = await response.json();
		if (!response.ok) {
			// catch all of the unhandled errors
			error_msg = 'Something went wrong. Please try again.';
			return;
		}
		is_solution = (JSONRes as CheckSolutionResponse).is_solution;
	}
</script>

<div class="relative w-full h-full flex flex-col items-center justify-center gap-32 md:flex-row">
	{#if error_msg != null}
		<div class="fixed right-10 top-10">
			<Toast
				clickHandler={() => {
					error_msg = null;
					info_msg = null;
				}}
				content={error_msg}
				buttonText="close"
			/>
		</div>
	{/if}
	{#if info_msg != null}
		<div class="fixed right-10 top-10">
			<Toast
				type="info"
				clickHandler={() => {
					error_msg = null;
					info_msg = null;
				}}
				content={info_msg}
				buttonText="close"
			/>
		</div>
	{/if}
	{#if is_solution == true}
		<div class="fixed right-10 top-10">
			<Toast
				type="success"
				clickHandler={() => {
					is_solution = null;
					info_msg = null;
					error_msg = null;
				}}
				content="Your solution is correct!"
				buttonText="close"
			/>
		</div>
	{:else if is_solution == false}
		<div class="fixed right-10 top-10">
			<Toast
				clickHandler={() => {
					is_solution = null;
					info_msg = null;
					error_msg = null;
				}}
				content="Your solution is wrong."
				buttonText="close"
			/>
		</div>
	{/if}

	<div>
		<div class="flex flex-row md:flex-col">
			{#each SIZES as size}
				<button
					class={`m-3 hover:opacity-50 hover:bg-neutral-300 ${
						selected_size == size ? 'bg-neutral-300 bg-opacity-70' : ''
					} p-1 rounded-lg`}
					on:click={() => {
						selected_size = size;
						board_state = generateEmptyBoard(size);
						error_msg = null;
						info_msg = null;
					}}
				>
					<p class="text-3xl font-semibold">
						{size}x{size}
					</p>
				</button>
			{/each}
		</div>
		<div class="flex flex-row md:flex-col gap-4">
			<Button 
				clickHandler={() => {
					error_msg = null;
					findSolutionHandler();
				}}
				content="solve"
				color="bg-blue-500"
			/>
			<Button 
				clickHandler={() => {
					error_msg = null;
					checkSolutionHandler();
				}}
				content="check"
				color="bg-green-500"
			/>
			<Button 
				clickHandler={() => {
					error_msg = null;
					board_state = generateEmptyBoard(selected_size);
				}}
				content="clear"
				color="bg-red-500"
			/>
		</div>
		<div class="mt-4 flex flex-col gap-2">
			<h3 class="font-semibold text-lg">share this puzzle:</h3>
			<CopyInput content={`${WEBSITE_URL}/board/${encodeBoardState(board_state)}`}/>
		</div>
	</div>

	<div class="flex flex-col gap-20">
		<h1 class="text-8xl font-bold">0h h1 solver</h1>
		<Board bind:board_state />
	</div>
</div>
