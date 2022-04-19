<script lang="ts">
    import {decodeBoardState} from '$src/lib/utils';
    import Board from '$components/board.svelte';
    import { page } from '$app/stores';
    import type { Board as BoardType } from '$src/types';

    let encoded_board = $page.params.encoded_board;
    let board_state: BoardType = decodeBoardState(encoded_board)
</script>

<div class="h-[30vw] w-[30vw]">
    <Board bind:board_state />
</div>