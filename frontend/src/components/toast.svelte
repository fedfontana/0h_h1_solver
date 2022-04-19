<script lang="ts">
	import { fade } from 'svelte/transition';
	import type { ToastType } from '../types';

	export let type: ToastType  = 'error';
	export let clickHandler: () => void;
	export let content: string = '';
	export let buttonText: string= '';

	let color: string = 'bg-red-500';
	let buttonColor: string = 'bg-red-200';
	if (type == 'info') {
		color = 'bg-blue-500';
		buttonColor = 'bg-blue-200';
	} else if (type == 'success') {
		color = 'bg-green-500';
		buttonColor = 'bg-green-200';
	}
</script>

<div
	class={`${color} text-xl min-h-[5rem] min-w-[20rem] flex items-center justify-center rounded-lg px-6 py-4 gap-4`}
	transition:fade={{ duration: 200 }}
>
	{content}
	<button
		class={`px-6 py-2 ${buttonColor} hover:opacity-80 hover:scale-[98%] rounded-lg text-lg font-bold`}
		on:click={clickHandler}>{buttonText}</button
	>
</div>
