<script>
    export let profiles = [];
  </script>
  
  <div class="bg-gray-100 p-4 rounded-lg mb-6">
    <h2 class="mb-4 text-xl font-bold">Анкеты других пользователей</h2>
    <div class="bg-gray-100 p-4 rounded-lg mb-6 h-screen overflow-y-auto">
      {#if profiles.length > 0}
        {#each profiles as profile}
          <div class="bg-gray-200 p-4 rounded-lg shadow mb-2">
            <h3 class="text-lg font-semibold text-gray-700">{profile.name}, {profile.age}</h3>
            <p class="text-gray-600">Национальность: {profile.nationality}</p>
            <p class="text-gray-600">Адрес: {profile.residence}</p>
            <p class="text-gray-600">Рост: {profile.height} см</p>
            <p class="text-gray-600">Дети: {profile.has_children ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">Образование: {profile.education ? 'Есть' : 'Нет'}</p>
            <p class="text-gray-600">Жильё: {profile.has_housing ? 'Есть' : 'Нет'}</p>
            <p class="text-gray-600">Родители: {profile.has_parents ? 'Есть' : 'Нет'}</p>
            <p class="text-gray-600">С родителями: {profile.livingplace ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">В браке: {profile.was_married ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">Судимость: {profile.has_criminal_record ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">Намаз: {profile.performs_namaz ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">Мазхаб: {profile.madhhab || 'Не указано'}</p>
            <p class="text-gray-600">Привычки: {profile.has_bad_habits || 'Нет'}</p>
            <p class="text-gray-600">Переезд: {profile.willing_to_relocate ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">Дети в планах: {profile.plan_to_have_children ? 'Да' : 'Нет'}</p>
            <p class="text-gray-600">Одежда: {profile.clothing_preferences || 'Не указано'}</p>
            <p class="text-gray-600">Здоровье: {profile.health || 'Не указано'}</p>
            <p class="text-gray-600">О себе: {profile.additional_info || 'Не указано'}</p>
            <p class="text-gray-600">Требования: {profile.spouse_requirements || 'Не указано'}</p>
          </div>
        {/each}
      {:else}
        <p class="text-gray-600">Анкет пока нет</p>
      {/if}
    </div>
  </div>