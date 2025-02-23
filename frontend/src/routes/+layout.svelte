<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { userStore, tokenStore, archiveStore, aboutStore, homeStore } from '$lib/stores';
  import Header from '../components/Header.svelte';
  import Footer from '../components/Footer.svelte';
  import { get } from 'svelte/store';

  let loading = true;
  let errorMessage = '';
  let currentPath = '';

  onMount(() => {
    currentPath = window.location.pathname;
    console.log('Текущий путь:', currentPath);
    loadData();
  });

  async function loadData() {
    const token = get(tokenStore);
    console.log('Токен:', token);

    if (currentPath === '/profile' && !token) {
      console.log('Нет токена для /profile, перенаправляем на /login');
      goto('/login');
      loading = false;
      return;
    }

    try {
      const sections = ['home', 'about', 'archive'];
      for (const section of sections) {
        console.log(`Загрузка данных для ${section}`);
        const response = await fetch(`http://localhost:8000/api/${section}/`);
        if (!response.ok) {
          const errorText = await response.text();
          console.error(`Ошибка загрузки ${section}: ${response.status} - ${errorText}`);
          if (section === 'home') homeStore.set([]);
          if (section === 'about') aboutStore.set([]);
          if (section === 'archive') archiveStore.set([]);
          continue;
        }
        const data = await response.json();
        if (section === 'home') homeStore.set(data);
        if (section === 'about') aboutStore.set(data);
        if (section === 'archive') archiveStore.set(data);
      }

      if (token && currentPath === '/profile') {
        console.log('Загрузка профиля с токеном:', token);
        const userResponse = await fetch('http://localhost:8000/api/profile/', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!userResponse.ok) {
          const errorText = await userResponse.text();
          console.error(`Ошибка загрузки профиля: ${userResponse.status} - ${errorText}`);
          userStore.set(null);
          if (userResponse.status === 401) {
            console.log('Токен недействителен, перенаправляем на /login');
            goto('/login');
          }
        } else {
          const profileData = await userResponse.json();
          console.log('Профиль загружен:', profileData);
          userStore.set(profileData);
        }
      }
    } catch (error) {
      console.error('Общая ошибка в loadData:', error.message);
      errorMessage = error.message;
    } finally {
      loading = false;
    }
  }
</script>

{#if loading}
  <div class="flex justify-center items-center min-h-screen">Загрузка...</div>
{:else if errorMessage}
  <div class="flex justify-center items-center min-h-screen text-red-500">
    Ошибка: {errorMessage}. Проверь консоль для деталей.
  </div>
{:else}
  <div class="flex flex-col min-h-screen bg-gray-100">
    <Header />
    <slot />
    <Footer />
  </div>
{/if}