<script lang="ts">
	import '$src/app.css';
	import Toast from '$components/toast.svelte';
	import { error_message, info_message, success_message, board_is_solution } from '$src/stores';

	$error_message = null;
	$info_message = null;
	$success_message = null;
	$board_is_solution = null;
</script>

<div class="relative w-full h-full flex flex-col py-12 md:w-8/12 mx-auto">
	<nav class="mb-5 md:mb-0">
		<h1 class="text-5xl md:text-8xl font-bold text-center w-full h-[8%]">
			<a href="/">0h h1 solver</a>
		</h1>
	</nav>
	<div class="relative">
		{#if $error_message != null}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					clickHandler={() => {
						$error_message = null;
						$info_message = null;
					}}
					content={$error_message}
					buttonText="close"
				/>
			</div>
		{/if}
		{#if $info_message != null}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					type="info"
					clickHandler={() => {
						$error_message = null;
						$info_message = null;
					}}
					content={$info_message}
					buttonText="close"
				/>
			</div>
		{/if}
		{#if $board_is_solution == true}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					type="success"
					clickHandler={() => {
						$board_is_solution = null;
						$info_message = null;
						$error_message = null;
					}}
					content="Your solution is correct!"
					buttonText="close"
				/>
			</div>
		{:else if $board_is_solution == false}
			<div class="md:fixed md:right-10 md:top-10">
				<Toast
					clickHandler={() => {
						$board_is_solution = null;
						$info_message = null;
						$error_message = null;
					}}
					content="Your solution is wrong."
					buttonText="close"
				/>
			</div>
		{/if}
	</div>
	<slot />
</div>
