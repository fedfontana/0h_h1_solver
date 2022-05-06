<script>
    import { theme, toggleTheme } from "$src/stores";
</script>

<div class="bg-neutral-200 w-8/12 h-4/6 flex flex-col items-center justify-between p-20">
    <h2 class="text-3xl font-bold h-1/5">
        Settings
    </h2>
    <div class="flex flex-col items-center justify-center h-4/5 w-full bg-red-200">
        <div>
            <input type="checkbox" name="dark theme switch" on:click={toggleTheme}>
            current theme: {$theme}
        </div>
        <div>
            <h3>Keyboard shorcuts</h3>
        </div>
        <div>
            credits
        </div>
    </div>
</div>