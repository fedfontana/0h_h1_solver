<script>
	import Board from '../components/board.svelte';

	const API_URL = 'http://localhost:5000';

	const SIZES = [4, 6, 8, 10, 12]
	let selected_size = 4

	let error_msg = null;

	let board_state = generateEmptyBoard(selected_size);

	function encodeBoardState(board_state) {
		return board_state.map(row => row.join(' ')).join(' | ');
	}

	function decodeBoardState(encoding) {
		let encoded_rows = encoding.split(' | ')
		return encoded_rows.map(encoded_row => encoded_row.split(' '));
	}

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

	function generateEmptyBoard(size) {
		let tmp = []
		for(let i = 0; i < size; i++) {
			let row = []
			for(let j = 0; j < size; j++)
				row.push('x');
			tmp.push(row);
		}
		return tmp;
	}
</script>

<div class="w-full h-full flex flex-col items-center justify-center gap-10">
	{#if error_msg != null}
		<div class="bg-red-500 text-xl">
			{error_msg}
			<button
				class="px-6 py-2 bg-red-200 hover:opacity-80 hover:scale-[98%]"
				on:click={() => {
					error_msg = null;
				}}>close</button
			>
		</div>
	{/if}
	<div>
		{#each SIZES as size}
			<button class="m-4 " on:click={() => {selected_size=size; board_state = generateEmptyBoard(size)}}>
				<p class="text-3xl font-semibold shadow-xl">
					{size}x{size}
				</p>
			</button>
		{/each}
	</div>

	<Board bind:board_state />
	<button
		class="px-6 py-2 bg-blue-500 hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-lg"
		on:click={findSolutionHandler}>find solution</button
	>
	<button
		class="px-6 py-2 bg-red-500 hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-md"
		on:click={() => {board_state = generateEmptyBoard(selected_size)}}>clear</button
	>
</div>