<script>
  import { tokenStore } from '$lib/stores';
  import Registration from './Registration.svelte';
  import IMask from 'imask'; // Исправленный импорт
  import { onMount } from 'svelte';

  let activeTab = 'login';
  let phoneNumber = '';
  let password = '';
  let error = '';
  let phoneInput;

  onMount(() => {
    IMask(phoneInput, {
      mask: '+7(000)000-00-00',
      lazy: false,
      placeholderChar: '_'
    });
  });

  async function handleLogin(event) {
    event.preventDefault();
    error = '';

    const cleanedPhone = phoneNumber.replace(/\D/g, '');
    if (!/^\d{11}$/.test(cleanedPhone) || !cleanedPhone.startsWith('7')) {
      error = 'Введите корректный номер телефона (11 цифр, начиная с +7)';
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/api/token/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          phone_number: phoneNumber,
          password: password
        })
      });

      const data = await response.json();
      if (response.ok) {
        tokenStore.set(data.access);
        console.log('Logged in successfully, token:', data.access);
        window.location.href = '/profile';
      } else {
        error = data.detail || 'Неверный номер телефона или пароль';
      }
    } catch (err) {
      error = 'Произошла ошибка при входе. Проверьте подключение.';
      console.error('Login error:', err);
    }
  }
</script>

<div class="min-h-screen bg-gray-100 flex items-center justify-center">
  <div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
    <div class="flex border-b mb-4">
      <button
        on:click={() => (activeTab = 'login')}
        class="w-1/2 py-2 text-center text-lg font-semibold border-b-2 transition-colors duration-300 hover:border-blue-500 hover:text-blue-500 {activeTab === 'login' ? 'border-blue-500 bg-indigo-50 text-blue-500' : 'border-transparent'}"
      >
        Вход
      </button>
      <button
        on:click={() => (activeTab = 'register')}
        class="w-1/2 py-2 text-center text-lg font-semibold border-b-2 transition-colors duration-300 hover:border-blue-500 hover:text-blue-500 {activeTab === 'register' ? 'border-blue-500 bg-indigo-50 text-blue-500' : 'border-transparent'}"
      >
        Регистрация
      </button>
    </div>

    {#if activeTab === 'login'}
      <form on:submit|preventDefault={handleLogin} class="space-y-4">
        <div>
          <label for="phoneNumber" class="block text-sm font-medium text-gray-700">Номер телефона</label>
          <input
            bind:this={phoneInput}
            bind:value={phoneNumber}
            class="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="+7(999)999-99-99"
            required
          />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input
            type="password"
            id="password"
            bind:value={password}
            class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        {#if error}
          <p class="text-red-500 text-sm">{error}</p>
        {/if}
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors"
        >
          Войти
        </button>
      </form>
    {:else if activeTab === 'register'}
      <Registration />
    {/if}
  </div>
</div>