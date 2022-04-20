/// <reference types="@sveltejs/kit" />

// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare namespace App {
	// interface Locals {}
	// interface Platform {}
	// interface Session {}
	// interface Stuff {}
}


//https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/typescript.md#im-using-an-attributeevent-on-a-dom-element-and-it-throws-a-type-error
declare namespace svelte.JSX {
    interface HTMLAttributes<T> extends AriaAttributes, DOMAttributes<T> {
        onerror_?: (event: any) => any;
        oninfo?: (event: any) => any;
        onsuccess?: (event: any) => any;
    }
}