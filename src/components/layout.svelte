<div class="h-[92%] w-full flex flex-col items-center justify-center gap-5 md:gap-12 md:flex-row">
    <div class="flex-[2] mx-auto w-full">
        <slot name="left"></slot>
    </div>
    <div class="flex flex-col w-full items-center justify-center flex-[4] md:flex-[6]">
        <slot name="center"></slot>
    </div>
    <div class="flex-[2] mt-5 md:mt-0">
        <slot name="right"></slot>
    </div>
</div>