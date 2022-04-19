<script lang="ts">
    import {decodeBoardState} from '../../lib/utils';
    import Board from '../../components/board.svelte';
    import { page } from '$app/stores';
    import type { Board as BoardType } from '../../types';

    let encoded_board = $page.params.encoded_board;
    let board_state: BoardType = decodeBoardState(encoded_board)
</script>

<Board bind:board_state />