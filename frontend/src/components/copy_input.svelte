<script lang="ts">
	import { fade } from 'svelte/transition';
	export let content: string = '';

	async function copyContent(): Promise<void> {
		try {
			await navigator.clipboard.writeText(content);
			showCopiedTooltip = true;
			setTimeout(() => {
				showCopiedTooltip = false;
			}, 800);
		} catch (err) {
			//$error_msg = "Couldn't copy the URL to your clipboard. Please try again."
		}
	}

	let showCopiedTooltip: boolean = false;
</script>

<div class="max-w-md flex">
	<input
		type="text"
		readonly
		class="rounded-l-md pl-4 pb-2 pt-3 bg-neutral-200 text-ellipsis text-lg"
		value={content}
	/>
	<button
		class="bg-neutral-200 px-3 rounded-r-md flex items-center content-center active:text-green-700"
		on:click={copyContent}
	>
		<div class="hover:translate-y-[-3px] duration-200 relative">
			{#if showCopiedTooltip}
				<span
					transition:fade={{ duration: 200 }}
					class="absolute top-6 right-[-32px] bg-neutral-700 text-neutral-100 px-3 py-1 rounded-md"
					>COPIED</span
				>
			{/if}
			<svg
				class="w-6 h-6"
				xmlns="http://www.w3.org/2000/svg"
				width="16"
				height="16"
				fill="currentColor"
				viewBox="0 0 16 16"
			>
				<path
					d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z"
				/>
				<path
					d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z"
				/>
			</svg>
		</div>
	</button>
</div>
