<script lang="ts">
	import { generateEmptyBoard } from '$src/lib/utils';
	import { error_message } from '$src/stores';
	import type { Board } from '$src/types';
	
	export let board_state = generateEmptyBoard(4);
	export let highlight_original: boolean = false;
	export let initial_state: Board | null = null;
	export let can_edit_board: boolean = true;
	export let can_edit_initial_state: boolean = true;

	if (
		(!can_edit_initial_state && initial_state === null) ||
		(highlight_original && initial_state === null)
	) {
		throw Error('Unacceptable comnbination of props');
	}

	if (
		initial_state !== null &&
		(initial_state.length !== board_state.length ||
			(initial_state.length > 0 && initial_state[0].length !== initial_state[0].length))
	) {
		throw Error('initial_board and board_state sizes must match');
	}

	function clickHandler(row_idx: number, col_idx: number, isRightClick: boolean): void {
		if (!can_edit_board) {
			$error_message = 'The board is read only.';
			return;
		}

		if (!can_edit_initial_state && initial_state![row_idx][col_idx] !== 'x') {
			$error_message = 'Cannot edit the initial state of the board';
			return;
		}

		if (board_state[row_idx][col_idx] == 'y') {
			board_state[row_idx][col_idx] = isRightClick ? 'x' : 'b';
		} else if (board_state[row_idx][col_idx] == 'b') {
			board_state[row_idx][col_idx] = isRightClick ? 'y' : 'x';
		} else if (board_state[row_idx][col_idx] == 'x') {
			board_state[row_idx][col_idx] = isRightClick ? 'b' : 'y';
		}
	}

	const board_classes_per_size = {
		'4': 'rounded-2xl md:rounded-3xl gap-2 md:gap-5',
		'6': 'rounded-xl md:rounded-2xl gap-1 md:gap-4',
		'8': 'rounded-[0.63rem] md:rounded-2xl gap-[0.2rem] md:gap-2',
		'10': 'rounded-lg md:rounded-xl gap-[0.125rem] md:gap-2',
		'12': 'rounded-md md:rounded-xl gap-[0.125rem] md:gap-1'
	};

	/* const lock_classes_per_size = {
		"4": "w-10 h-10 md:w-12 h-12",
		"6": "w-10 h-10 md:w-10 h-10",
		"8": "w-10 h-10 md:w-10 h-10",
		"10": "w-10 h-10 md:w-8 h-8",
		"12": "w-10 h-10 md:w-10 h-10"
	} */
</script>

<!--TODO fix bugs:
- quando si sceglie una size, si risovle e si selezionano i lucchetti, poi quando si cambia size si puo'
 cambiare size solo per una prima volta e la board viene tutta fuckappata
- quando si selezionano i lock poi non si possono togliere (stato non viene riflesso su board) 
- non so come siano le size dei lock su mobile

-->

<div
	class={`flex flex-col h-full w-full justify-between ${
		board_classes_per_size[board_state.length]
	}`}
	on:contextmenu|preventDefault
>
	{#each board_state as row, row_idx}
		<div
			class={`flex flex-row w-full justify-between flex-1 ${
				board_classes_per_size[board_state.length]
			}`}
		>
			{#each row as tile, col_idx}
				<div
					class={`${
						tile == 'y' ? 'bg-[#ffd700]' : tile == 'b' ? 'bg-[#0057b7]' : 'bg-neutral-700'
					} flex-1 ${
						board_classes_per_size[board_state.length]
					} shadow-lg transition-colors duration-200
					${
						can_edit_board &&
						!can_edit_initial_state &&
						initial_state !== null &&
						initial_state[row_idx][col_idx] === 'x'
							? 'hover:opacity-80 hover:scale-[98%]'
							: ''
					}
					flex items-center justify-center`}
					on:click={() => clickHandler(row_idx, col_idx, false)}
					on:contextmenu|preventDefault={() => clickHandler(row_idx, col_idx, true)}
				>
					{#if highlight_original && initial_state !== null && initial_state[row_idx][col_idx] !== 'x'}
						<svg
							class="w-[40%] h-[40%]"
							xmlns="http://www.w3.org/2000/svg"
							width="16"
							height="16"
							fill="currentColor"
							viewBox="0 0 16 16"
						>
							<path
								d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"
							/>
						</svg>
					{/if}
				</div>
			{/each}
		</div>
	{/each}
</div>

<!--  -->
