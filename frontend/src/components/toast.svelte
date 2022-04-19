<script lang="ts">
	import { fade } from 'svelte/transition';
	import type { ToastType } from '$src/types';

	export let type: ToastType  = 'error';
	export let clickHandler: () => void;
	export let content: string = '';
	export let buttonText: string= '';

	let color: string = 'red';
	if (type == 'info') {
		color = 'blue';
	} else if (type == 'success') {
		color = 'green';
	}
</script>

<div
	class={`bg-${color}-500 text-xl min-h-[5rem] min-w-[20rem] flex items-center justify-center rounded-lg px-6 py-4 gap-4`}
	transition:fade={{ duration: 200 }}
>
	{content}
	<button
		class={`px-6 py-2 bg-${color}-200 hover:opacity-80 hover:scale-[98%] rounded-lg text-lg font-bold`}
		on:click={clickHandler}>{buttonText}</button
	>
</div>
