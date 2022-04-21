<script lang="ts">
	import '$src/app.css';

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	import { error_message, info_message, board_is_solution } from '$src/stores';

	import Toast from '$components/toast.svelte';

	$error_message = null;
	$info_message = null;
	$board_is_solution = null;

	onMount(() => {
		window.onunhandledrejection = () => {
			goto("/error");
		}
	})
</script>

<div class="relative w-full flex flex-col py-12 md:w-8/12 mx-auto md:h-[95%]">
	<nav class="mb-5 md:mb-0">
		<h1 class="text-5xl md:text-8xl font-bold text-center w-full h-[8%]">
			<a href="/">0h h1 solver</a>
		</h1>
	</nav>
	<div class="relative">
		{#if $error_message != null}
			<div class="w-[90%] mx-auto mb-5 md:mb-0 md:w-auto md:fixed md:right-10 md:top-10">
				<Toast
					click_handler={() => {
						$error_message = null;
						$info_message = null;
					}}
					content={$error_message}
					button_content="close"
				/>
			</div>
		{/if}
		{#if $info_message != null}
			<div class="w-[90%] mx-auto mb-5 md:mb-0 md:w-auto md:fixed md:right-10 md:top-10">
				<Toast
					type="info"
					click_handler={() => {
						$error_message = null;
						$info_message = null;
					}}
					content={$info_message}
					button_content="close"
				/>
			</div>
		{/if}
		{#if $board_is_solution == true}
			<div class="w-[90%] mx-auto mb-5 md:mb-0 md:w-auto md:fixed md:right-10 md:top-10">
				<Toast
					type="success"
					click_handler={() => {
						$board_is_solution = null;
						$info_message = null;
						$error_message = null;
					}}
					content="Your solution is correct!"
					button_content="close"
				/>
			</div>
		{:else if $board_is_solution == false}
			<div class="w-[90%] mx-auto mb-5 md:mb-0 md:w-auto md:fixed md:right-10 md:top-10">
				<Toast
					click_handler={() => {
						$board_is_solution = null;
						$info_message = null;
						$error_message = null;
					}}
					content="Your solution is wrong."
					button_content="close"
				/>
			</div>
		{/if}
	</div>
	<slot />
</div>
<footer class="flex w-full justify-center text-center items-center pb-5 md:h-[5%]">
	<p class="text-lg">made with 🧩 by <a class="text-blue-500 hover:underline decoration-2" href="https://fedfontana.dev">fedfontana</a>. Source code available on <a class="text-blue-500 hover:underline decoration-2" href="https://github.com/fedfontana/0h_h1_solver">github</a></p>
</footer>