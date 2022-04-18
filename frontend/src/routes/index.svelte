<script>
	import Board from '../components/board.svelte';
	import Pill from '../components/pill.svelte';
	import { encodeBoardState, decodeBoardState, generateEmptyBoard } from '../lib/utils';
	const API_URL = 'http://localhost:5000';
	const WEBSITE_URL = 'http://localhost:3000';

	const SIZES = [4, 6, 8, 10, 12];
	let selected_size = 4;

	let error_msg = null;

	let board_state = generateEmptyBoard(selected_size);

	async function findSolutionHandler() {
		let response = await fetch(`${API_URL}/get_solution/${encodeBoardState(board_state)}`);
		let status = response.status;
		let JSONRes = await response.json();
		if (status == 404) {
			// no solution found
			error_msg = JSONRes.error_message;
			return;
		}
		if (!response.ok) {
			// catch all of the unhandled errors
			error_msg = 'Something went wrong. Please try again.';
			return;
		}
		board_state = decodeBoardState(JSONRes.solution);
	}
</script>

<div class="relative w-full h-full flex flex-col items-center justify-center gap-32 md:flex-row">
	{#if error_msg != null}
		<div class="fixed right-10 top-10">
			<Pill clickHandler={() => {
				error_msg = null;
			}}
			content={error_msg}
			buttonText="close"/>
		</div>
	{/if}
	<div>
		<div class="flex flex-row md:flex-col">
			{#each SIZES as size}
				<button
					class={`m-3 hover:opacity-50 hover:bg-neutral-300 ${selected_size == size ? "bg-neutral-300 bg-opacity-70" : ""} p-1 rounded-lg`}
					on:click={() => {
						selected_size = size;
						board_state = generateEmptyBoard(size);
						error_msg = null;
					}}
				>
					<p class="text-3xl font-semibold">
						{size}x{size}
					</p>
				</button>
			{/each}
		</div>
		<div class="flex flex-row md:flex-col gap-4">
			<button
				class="px-6 py-2 bg-blue-500 hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-lg font-bold"
				on:click={findSolutionHandler}>solve</button
			>
			<button
				class="px-6 py-2 bg-green-500 hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-lg font-bold"
			>
				check
			</button>
			<button
				class="px-6 py-2 bg-red-500 hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-lg font-bold"
				on:click={() => {
					board_state = generateEmptyBoard(selected_size);
					error_msg = null;
				}}>clear</button
			>
		</div>
		<div class="mt-4 flex flex-col gap-2">
			<h3 class="font-semibold text-lg">
				share this puzzle:
			</h3>
			<div class="max-w-md flex">
				<input type="text" readonly class="rounded-l-md pl-4 py-2 bg-neutral-200 text-ellipsis" value={`${WEBSITE_URL}/board/${encodeBoardState(board_state)}`}>
				<button class="bg-neutral-500 px-3 rounded-r-md">cp</button>
			</div>
		</div>
	</div>

	<div class="flex flex-col gap-20">
		<h1 class="text-8xl font-bold">0h h1 solver</h1>
		<Board bind:board_state />
	</div>
</div>
