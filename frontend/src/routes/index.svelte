<script>
	import Board from '../components/board.svelte';

	const API_URL = 'http://localhost:5000';

	let error_msg = null;

	let board_state = [
		['y', 'b'],
		['b', 'y']
	];

	function encodeBoardState(board_state) {
		return '';
	}

	function decodeBoardState(encoding) {
		return [
			['x', 'x'],
			['x', 'x']
		];
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
	<Board bind:board_state />
	<button
		class="px-6 py-2 bg-blue-500 hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-lg"
		on:click={findSolutionHandler}>find solution</button
	>
</div>
