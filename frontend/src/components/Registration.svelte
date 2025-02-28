<script lang="ts">
  import { goto } from '$app/navigation';
  import { tokenStore } from '$lib/stores';
  import IMask from 'imask';
  import { onMount } from 'svelte';

  let formData = {
    phone_number: '',
    password: '',
    confirmPassword: ''
  };
  let errors = {
    phone_number: '',
    password: '',
    confirmPassword: '',
    server: ''
  };
  let isSubmitting = false;
  let phoneInput: HTMLInputElement;
  let mask: IMask.InputMask<IMask.AnyMaskedOptions>;

  onMount(() => {
    mask = IMask(phoneInput, {
      mask: '8(000)000-00-00', // Маска с 8 вместо +7
      lazy: false,
      placeholderChar: '_',
      overwrite: true // Перезаписывает в рамках маски
    });
  });

  function validateForm(): boolean {
    errors = { phone_number: '', password: '', confirmPassword: '', server: '' };
    const cleanedPhone = formData.phone_number.replace(/\D/g, ''); // Убираем всё, кроме цифр
    const trimmedPhone = cleanedPhone.slice(0, 11); // Обрезаем до 11 цифр (8 + 10)

    // Проверяем ровно 11 цифр, начиная с 8
    if (!/^8\d{10}$/.test(trimmedPhone)) {
      errors.phone_number = 'Введите корректный номер телефона (10 цифр после 8).';
    }

    if (formData.password !== formData.confirmPassword) {
      errors.confirmPassword = 'Пароли не совпадают.';
    }

    return Object.values(errors).every(e => e === '');
  }

  async function handleSubmit(event: Event): Promise<void> {
    event.preventDefault();
    if (!validateForm()) return;

    isSubmitting = true;
    try {
      const cleanedPhone = formData.phone_number.replace(/\D/g, '');
      const trimmedPhone = cleanedPhone.slice(0, 11); // Обрезаем до 11 цифр

      const response = await fetch('http://localhost:8000/api/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          phone_number: trimmedPhone, // 89998887766
          password: formData.password
        })
      });

      const data = await response.json();
      console.log('Ответ сервера:', data);
      if (response.ok) {
        console.log('Регистрация успешна, токен:', data.access);
        tokenStore.set(data.access || null);
        console.log('Токен сохранён, перенаправляем на /profile');
        window.location.href = '/profile';
      } else {
        errors.server = data.error || 'Ошибка регистрации';
        console.log('Ошибка регистрации:', errors.server);
      }
    } catch (err) {
      errors.server = 'Ошибка соединения с сервером.';
      console.error('Registration error:', err);
    } finally {
      isSubmitting = false;
    }
  }
</script>

<div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md mx-auto">
  <h1 class="text-2xl font-bold mb-4 text-center">Регистрация</h1>
  <form on:submit|preventDefault={handleSubmit} class="space-y-4">
    <div>
      <label for="phone_number" class="block text-sm font-medium text-gray-700">Номер телефона</label>
      <input
        bind:this={phoneInput}
        bind:value={formData.phone_number}
        class="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
        placeholder="8(999)999-99-99"
        required
      />
      {#if errors.phone_number}
        <p class="text-red-500 text-sm mt-1">{errors.phone_number}</p>
      {/if}
    </div>
    <div>
      <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
      <input
        type="password"
        id="password"
        bind:value={formData.password}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
        required
      />
      {#if errors.password}
        <p class="text-red-500 text-sm mt-1">{errors.password}</p>
      {/if}
    </div>
    <div>
      <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Подтверждение пароля</label>
      <input
        type="password"
        id="confirmPassword"
        bind:value={formData.confirmPassword}
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
        required
      />
      {#if errors.confirmPassword}
        <p class="text-red-500 text-sm mt-1">{errors.confirmPassword}</p>
      {/if}
    </div>
    {#if errors.server}
      <p class="text-red-500 text-sm mt-1">{errors.server}</p>
    {/if}
    <button
      type="submit"
      class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors"
      disabled={isSubmitting}
    >
      {isSubmitting ? 'Отправка...' : 'Зарегистрироваться'}
    </button>
  </form>
</div>