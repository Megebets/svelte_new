<script>
    import { onMount, onDestroy } from 'svelte';
  
    export let tips = [];
    let currentTipIndex = 0;
  
    function updateTip() {
      if (tips.length > 0) {
        currentTipIndex = (currentTipIndex + 1) % tips.length;
      }
    }
  
    let intervalId;
    onMount(() => {
      intervalId = setInterval(updateTip, 30000); // Смена каждые 30 секунд
    });
  
    onDestroy(() => {
      clearInterval(intervalId);
    });
  </script>
  
  <div class="bg-gray-100 p-4 rounded-lg mb-6">
    <h2 class="mb-4 text-xl font-bold">Полезные советы</h2>
    {#if tips.length > 0}
      <div class="bg-gray-200 p-4 rounded-lg shadow">
        <h3 class="text-lg font-semibold text-gray-700">{tips[currentTipIndex].title}</h3>
        <p class="text-gray-600">{tips[currentTipIndex].description}</p>
      </div>
    {:else}
      <p class="text-gray-600">Советов пока нет</p>
    {/if}
  </div>