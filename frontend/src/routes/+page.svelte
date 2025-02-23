<script>
  import { homeStore } from '$lib/stores';
  import Modal from '../components/Modal.svelte';
  import ContactInfo from '../components/ContactInfo.svelte';
  import AuthForm from '../components/AuthForm.svelte';
  import Registration from '../components/Registration.svelte';

  let activeModal = '';
  $: homeData = $homeStore || [];

  const openModal = (type) => {
    activeModal = type;
  };

  const closeModal = () => {
    activeModal = '';
  };

  const news = [
    { title: 'Новость 1', description: 'Краткое описание новости.' },
    { title: 'Новость 2', description: 'Краткое описание новости.' }
  ];
  const articles = [
    { title: 'Статья 1', description: 'Краткое описание статьи.' },
    { title: 'Статья 2', description: 'Краткое описание статьи.' }
  ];
</script>

<main class="flex-grow p-6 bg-white">
  <section class="mb-10">
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Наши истории</h2>
    {#if homeData.length > 0}
      <div class="relative bg-gray-200 h-64 rounded-lg overflow-hidden">
        {#each homeData as item, index}
          <div class="{index === 0 ? 'block' : 'hidden'} absolute inset-0 w-full h-full">
            <img src={item.image || '/images/default.jpg'} alt={item.title} class="w-full h-full object-cover" />
            <div class="absolute bottom-0 p-4 bg-black bg-opacity-50 text-white w-full">
              <h3 class="text-lg font-semibold">{item.title}</h3>
              <p>{item.text}</p>
            </div>
          </div>
        {/each}
      </div>
    {:else}
      <div class="bg-gray-200 h-64 rounded-lg flex items-center justify-center text-gray-500">
        Здесь будет карусель...
      </div>
    {/if}
  </section>

  <section class="mb-10">
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Последние новости</h2>
    <div class="space-y-4">
      {#each news as item}
        <div class="bg-gray-100 p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-700">{item.title}</h3>
          <p class="text-gray-600">{item.description}</p>
        </div>
      {/each}
    </div>
  </section>

  <section>
    <h2 class="text-2xl font-bold text-gray-800 mb-4">Популярные статьи</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      {#each articles as item}
        <div class="bg-gray-100 p-4 rounded-lg shadow">
          <h3 class="text-lg font-semibold text-gray-700">{item.title}</h3>
          <p class="text-gray-600">{item.description}</p>
        </div>
      {/each}
    </div>
  </section>

  {#if activeModal === 'contact'}
    <Modal on:close={closeModal}>
      <ContactInfo />
    </Modal>
  {/if}
  {#if activeModal === 'auth'}
    <Modal on:close={closeModal}>
      <AuthForm />
    </Modal>
  {/if}
  {#if activeModal === 'registration'}
    <Modal on:close={closeModal}>
      <Registration />
    </Modal>
  {/if}
</main>