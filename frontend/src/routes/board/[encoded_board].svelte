<script>
    import {decodeBoardState} from '../../lib/utils';
    import Board from '../../components/board.svelte';
    import { page } from '$app/stores';
    let encoded_board = $page.params.encoded_board;
    let board_state = decodeBoardState(encoded_board)
</script>

<Board bind:board_state />