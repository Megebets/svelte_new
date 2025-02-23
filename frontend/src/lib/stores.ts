// frontend/src/lib/stores.ts
import { writable } from 'svelte/store';
import { browser } from '$app/environment';

export const userStore = writable(null);
export const archiveStore = writable([]);
export const aboutStore = writable([]);
export const homeStore = writable([]);
export const tokenStore = writable(browser ? localStorage.getItem('token') || null : null);

if (browser) {
  tokenStore.subscribe((value) => {
    if (value) localStorage.setItem('token', value);
    else localStorage.removeItem('token');
  });
}
