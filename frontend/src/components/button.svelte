<script lang="ts">
	export let clickHandler: () => void;
	export let content: string;
	export let color: string;
	export let disabled: boolean = false;
</script>

<button
	disabled={disabled}
	class={`px-6 py-2 ${color} hover:opacity-80 hover:scale-[98%] shadow-md rounded-lg text-xl font-bold`}
	on:click={clickHandler}
>
	{content}
</button>
