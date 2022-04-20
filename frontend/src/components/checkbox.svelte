<script lang="ts">
	export let disabled: boolean = false;
	export let checked: boolean = false;
	export let size: number = 2;
</script>

<div
	class={`rounded-lg ${disabled ? 'bg-neutral-400': checked ? 'bg-green-500' : ''} ${disabled ? 'border-neutral-500' : 'cursor-pointer'} border-[3px] border-neutral-600 flex items-center justify-center `}
	style="width: {size}rem; height: {size}rem;"
	on:click={() => {
		if (disabled) return;
		checked = !checked;
	}}
>
	{#if checked}
		<svg
			class="h-[200%] w-[200%] text-white"
			xmlns="http://www.w3.org/2000/svg"
			width="16"
			height="16"
			fill="currentColor"
			viewBox="0 0 16 16"
		>
			<path
				d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"
			/>
		</svg>
	{/if}
</div>
