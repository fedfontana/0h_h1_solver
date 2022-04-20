<script>
    import { decodeBoardState } from "$lib/utils";

    import Board from "$src/components/board.svelte";
    
    const error_board = decodeBoardState('yyyxbbxxyyxx-yxxxbxbxyxyx-yyxxbbxxyyxx-yxxxbxbxyxyx-yyyxbxbxyxyx-xxxxxxxxxxxx-xxxxxxxxxxxx-xxbbbxyyxxxx-xxbxbxyxyxxx-xxbxbxyyxxxx-xxbxbxyxyxxx-xxbbbxyxyxxx');
</script>

<div class="flex flex-col items-center justify-center gap-16 h-[92%]">
    <div 
    on:error_|stopPropagation class="w-[75vw] h-[75vw] md:w-[25vw] md:h-[25vw]">
        <Board board_state={error_board} readonly={true} />
    </div>
    <div class="flex flex-col items-center gap-8">
        <h2 class="text-4xl font-semibold">This is now the page you are looking for</h2>
        <a class="text-3xl hover:underline hover:decoration-4 text-blue-500" href="/">Go back to the home page</a>
    </div>
</div>
