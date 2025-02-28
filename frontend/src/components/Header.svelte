<script>
  import AuthModal from './AuthForm.svelte';
  let showModal = false; // Состояние модального окна
  let showMenu = false; // Состояние мобильного меню

  // Функция для закрытия модального окна при клике на ссылку
  function closeModalAndNavigate(url) {
    showModal = false;
    window.location.href = url;
  }
</script>

<header>
  <section class="flex justify-between bg-gray-800 text-white p-4">
    <!-- Логотип -->
    <div class="flex items-center">
      <img src="/images/logo.jpg" alt="Логотип моего сайта" class="h-16 w-16">
    </div>

    <!-- Название и описание -->
    <div class="flex flex-col text-center mx-auto">
      <h1 class="text-2xl font-bold whitespace-nowrap">"УЮТ"</h1>
      <h2 class="text-lg text-gray-300 whitespace-nowrap">Институт семейного счастья</h2>
    </div>

    <!-- Кнопка меню для мобильных устройств -->
    <button
      class="block md:hidden bg-gray-700 p-2 rounded"
      on:click={() => (showMenu = !showMenu)}
    >
      ☰
    </button>

    <!-- Навигация -->
    <nav class="hidden md:block">
      <ul class="flex space-x-6 text-base">
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/" on:click|preventDefault={() => closeModalAndNavigate('/')}>Главная</a>
        </li>
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/contacts" on:click|preventDefault={() => closeModalAndNavigate('/contacts')}>Контакты</a>
        </li>
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/about" on:click|preventDefault={() => closeModalAndNavigate('/about')}>О нас</a>
        </li>
        <li class="hover:text-green-200 hover:scale-125 transition duration-200">
          <a href="/archive" on:click|preventDefault={() => closeModalAndNavigate('/archive')}>Архив</a>
        </li>
        <li class="bg-blue-500 hover:text-green-200 text-white px-6 py-2 rounded-lg hover:scale-105 transition duration-200">
          <button on:click={() => (showModal = true)}>Войти</button>
        </li>
      </ul>
    </nav>
  </section>

  <!-- Мобильное меню -->
  {#if showMenu}
    <div class="md:hidden bg-gray-800 p-4">
      <ul class="space-y-4">
        <li><a href="/" on:click|preventDefault={() => closeModalAndNavigate('/')} class="text-white hover:text-green-200">Главная</a></li>
        <li><a href="/contacts" on:click|preventDefault={() => closeModalAndNavigate('/contacts')} class="text-white hover:text-green-200">Контакты</a></li>
        <li><a href="/about" on:click|preventDefault={() => closeModalAndNavigate('/about')} class="text-white hover:text-green-200">О нас</a></li>
        <li><a href="/archive" on:click|preventDefault={() => closeModalAndNavigate('/archive')} class="text-white hover:text-green-200">Архив</a></li>
        <li>
          <button on:click={() => (showModal = true)} class="bg-blue-500 text-white px-6 py-2 rounded-lg">
            Войти
          </button>
        </li>
      </ul>
    </div>
  {/if}
</header>

<!-- Модальное окно -->
{#if showModal}
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50" on:click={() => (showModal = false)}>
    <div class="bg-white rounded-lg p-4 w-full max-w-md shadow-lg" on:click|stopPropagation>
      <AuthModal on:close={() => (showModal = false)} />
    </div>
  </div>
{/if}

<style lang="postcss">
  @media (max-width: 768px) {
    nav ul {
      @apply hidden; /* Скрываем обычное меню на мобильных устройствах */
    }
  }
</style>