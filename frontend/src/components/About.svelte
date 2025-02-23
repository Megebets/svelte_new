<script>
  import { aboutStore } from '$lib/stores';

  $: aboutData = $aboutStore || [];
</script>

<div class="container mx-auto p-4">
  <h1 class="text-2xl font-bold mb-6">О нас</h1>
  <div class="grid gap-6">
    {#each aboutData as item}
      <div class="border rounded-lg p-4 shadow">
        <h2 class="text-xl font-semibold">{item.title}</h2>
        {#if item.date}
          <p class="text-gray-500">{item.date}</p>
        {/if}
        <p class="text-gray-700 mt-2">{item.text}</p>
        {#if item.image}
          <img src={item.image} alt={item.title} class="mt-4 w-full h-48 object-cover rounded" />
        {/if}
      </div>
    {/each}
  </div>
</div>