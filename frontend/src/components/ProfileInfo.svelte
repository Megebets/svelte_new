<script>
    import IMask from 'imask';
    import { onMount, tick } from 'svelte';
    import { tokenStore } from '$lib/stores';
  
    export let userData;
    export let onSave;
    export let onCancel;
  
    let profileCompletion = 0;
    /** @type {HTMLInputElement | null} */
    let phoneInput = null;
    /** @type {HTMLInputElement | null} */
    let trustedPhoneInput = null;
  
    function validateForm() {
      if (!userData.name) {
        alert('Пожалуйста, укажите имя');
        return false;
      }
      if (!userData.consent_to_data_processing) {
        alert('Необходимо согласие на обработку персональных данных');
        return false;
      }
      return true;
    }
  
    async function saveProfile(event) {
      event.preventDefault();
      if (!validateForm()) return;
  
      try {
        const response = await fetch('http://localhost:8000/api/profile/', {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${$tokenStore}`
          },
          body: JSON.stringify(userData)
        });
        if (!response.ok) {
          const errorText = await response.text();
          throw new Error(`Ошибка при сохранении данных: ${response.status} - ${errorText}`);
        }
        const data = await response.json();
        onSave(data);
      } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка при сохранении данных.');
      }
    }
  
    function calculateCompletion() {
      const totalFields = Object.keys(userData).length;
      const filledFields = Object.values(userData).filter(
        (value) => value !== '' && value !== null && value !== false && value !== 0
      ).length;
      profileCompletion = Math.round((filledFields / totalFields) * 100);
    }
  
    function getProgressHint() {
      if (profileCompletion < 80) {
        return 'Пока ваша анкета не заполнена, ее не будут рассматривать наши специалисты';
      } else if (profileCompletion >= 80 && profileCompletion < 100) {
        return 'Чем точнее и объемнее будут ваши данные, тем быстрее мы сможем вам помочь';
      }
      return '';
    }
  
    onMount(async () => {
      calculateCompletion();
      await tick();
      if (phoneInput) {
        IMask(phoneInput, { mask: '+7(000)000-00-00', lazy: false, placeholderChar: '_' });
      }
      if (trustedPhoneInput) {
        IMask(trustedPhoneInput, { mask: '+7(000)000-00-00', lazy: false, placeholderChar: '_' });
      }
    });
  
    $: if (!userData.has_children) {
      userData.children_boys = 0;
      userData.children_girls = 0;
      userData.children_ages = '';
    }
  </script>
  
  <form class="mx-auto max-w-2xl rounded-md bg-gray-100 p-6 shadow-md" on:submit={saveProfile}>
    <h2 class="mb-4 text-xl font-semibold">Редактирование анкеты</h2>
    <div class="grid grid-cols-1 gap-4">
      <div class="group border-2 bg-white bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Фамилия</label>
        <input
          type="text"
          bind:value={userData.last_name}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Имя</label>
        <input
          type="text"
          bind:value={userData.name}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Отчество</label>
        <input
          type="text"
          bind:value={userData.middle_name}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Пол</label>
        <select
          bind:value={userData.pol}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value="">Выберите пол</option>
          <option value="Мужской">Мужской</option>
          <option value="Женский">Женский</option>
        </select>
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Дата рождения</label>
        <input
          type="date"
          bind:value={userData.birthdate}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Место рождения</label>
        <input
          type="text"
          bind:value={userData.birthplace}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Национальность</label>
        <input
          type="text"
          bind:value={userData.nationality}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Адрес проживания</label>
        <input
          type="text"
          bind:value={userData.residence}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Контактный телефон</label>
        <input
          bind:this={phoneInput}
          bind:value={userData.contact_phone}
          class="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="+7(999)999-99-99"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Телефон доверенного лица</label>
        <input
          bind:this={trustedPhoneInput}
          bind:value={userData.trusted_person_phone}
          class="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="+7(999)999-99-99"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Рост (см)</label>
        <input
          type="number"
          bind:value={userData.height}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Имеются ли дети?</label>
        <select
          bind:value={userData.has_children}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
        {#if userData.has_children}
          <div>
            <label class="block text-sm font-medium text-gray-700">Сколько мальчиков?</label>
            <input
              type="number"
              bind:value={userData.children_boys}
              class="mt-1 block w-full rounded-md border-gray-300"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Сколько девочек?</label>
            <input
              type="number"
              bind:value={userData.children_girls}
              class="mt-1 block w-full rounded-md border-gray-300"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Возраст детей</label>
            <input
              type="text"
              bind:value={userData.children_ages}
              class="mt-1 block w-full rounded-md border-gray-300"
              placeholder="Например: 5, 7, 10"
            />
          </div>
        {/if}
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Образование</label>
        <select bind:value={userData.education} class="mt-1 block w-full rounded-md border-gray-300">
          <option value={false}>Нет</option>
          <option value={true}>Есть</option>
        </select>
        {#if userData.education}
          <div>
            <label class="block text-sm font-medium text-gray-700">Какой уровень?</label>
            <select bind:value={userData.education_level} class="mt-1 block w-full rounded-md border-gray-300">
              <option value="">Выберите уровень</option>
              <option value="высшее">Высшее</option>
              <option value="среднее специальное">Среднее специальное</option>
            </select>
          </div>
          {#if userData.education_level}
            <div>
              <label class="block text-sm font-medium text-gray-700">Специальность</label>
              <input
                type="text"
                bind:value={userData.specialty}
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
              />
            </div>
          {/if}
        {/if}
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">У вас есть собственное жилье?</label>
        <select
          bind:value={userData.has_housing}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Есть</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">У вас есть родители?</label>
        <select
          bind:value={userData.has_parents}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Есть</option>
        </select>
        {#if userData.has_parents}
          <div>
            <label class="block text-sm font-medium text-gray-700">Вы проживаете с родителями?</label>
            <select
              bind:value={userData.livingplace}
              class="mt-1 block w-full rounded-md border-gray-300"
            >
              <option value={false}>Я живу один</option>
              <option value={true}>Я проживаю с родителями</option>
            </select>
          </div>
        {/if}
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Вы работаете?</label>
        <select
          bind:value={userData.has_working}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Не работаю</option>
          <option value={true}>Работаю</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Вы состояли в браке?</label>
        <select
          bind:value={userData.was_married}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">У вас есть судимость?</label>
        <select
          bind:value={userData.has_criminal_record}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Есть</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Вы совершаете намаз?</label>
        <select
          bind:value={userData.performs_namaz}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Какого мазхаба придерживаетесь?</label>
        <select
          bind:value={userData.madhhab}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value="">Не выбрано</option>
          <option value="ханафитский">Ханафитский</option>
          <option value="маликитский">Маликитский</option>
          <option value="шафиитский">Шафиитский</option>
          <option value="ханбалитский">Ханбалитский</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Какие вредные привычки присущи вам?</label>
        <input
          type="text"
          bind:value={userData.has_bad_habits}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Возможен брак с разведённым(ой)?</label>
        <select
          bind:value={userData.ok_with_divorced_spouse}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Возможен ли брак с человеком, у которого есть дети?</label>
        <select
          bind:value={userData.ok_with_spouse_children}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Готовы ли к переезду?</label>
        <select
          bind:value={userData.willing_to_relocate}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
      </div>
  
      {#if userData.pol === "Женский"}
        <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
          <label class="block text-sm font-medium text-gray-700">Согласна быть второй женой?</label>
          <select
            bind:value={userData.agree_to_be_second_wife}
            class="mt-1 block w-full rounded-md border-gray-300"
          >
            <option value={false}>Нет</option>
            <option value={true}>Да</option>
          </select>
        </div>
      {/if}
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Планируете детей?</label>
        <select
          bind:value={userData.plan_to_have_children}
          class="mt-1 block w-full rounded-md border-gray-300"
        >
          <option value={false}>Нет</option>
          <option value={true}>Да</option>
        </select>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Ваши предпочтения в одежде:</label>
        <input
          type="text"
          bind:value={userData.clothing_preferences}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Возраст будущего(ей) супруга(и)</label>
        <div class="flex gap-2">
          <input
            type="number"
            bind:value={userData.spouse_age_min}
            min="18"
            max="100"
            class="mt-1 w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            placeholder="От"
          />
          <input
            type="number"
            bind:value={userData.spouse_age_max}
            min="18"
            max="100"
            class="mt-1 w-1/2 rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            placeholder="До"
          />
        </div>
      </div>
  
      <div class="group rounded-lg bg-white border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Состояние вашего здоровья:</label>
        <input
          type="text"
          bind:value={userData.health}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        />
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">О себе</label>
        <textarea
          bind:value={userData.additional_info}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        ></textarea>
      </div>
  
      <div class="group border-2 bg-white border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
        <label class="block text-sm font-medium text-gray-700">Требования к супругу</label>
        <textarea
          bind:value={userData.spouse_requirements}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
        ></textarea>
      </div>
  
      <div class="mt-4">
        <label class="inline-flex items-center">
          <input
            type="checkbox"
            bind:checked={userData.consent_to_data_processing}
            class="form-checkbox h-5 w-5 text-indigo-600"
          />
          <span class="ml-2 text-gray-700">Согласен(а) на обработку персональных данных</span>
        </label>
      </div>
  
      <div class="mt-6">
        <h2 class="mb-4 text-xl font-bold inline-block">Заполнение анкеты</h2>
        <span class="text-sm text-gray-600 ml-2">{getProgressHint()}</span>
        <div class="relative pt-1">
          <div class="mb-2 flex items-center justify-between">
            <span class="inline-block rounded-full bg-indigo-200 px-2 py-1 text-xs font-semibold uppercase text-indigo-600">
              {profileCompletion}%
            </span>
          </div>
          <div class="mb-4 flex h-2 overflow-hidden rounded bg-indigo-200 text-xs">
            <div
              style="width: {profileCompletion}%"
              class="flex flex-col justify-center whitespace-nowrap bg-indigo-500 text-center text-white shadow-none"
            ></div>
          </div>
        </div>
      </div>
  
      <div class="mt-6 flex justify-between gap-4">
        <button type="button" class="rounded bg-gray-500 px-4 py-2 text-white" on:click={onCancel}>
          Отмена
        </button>
        <button
          type="submit"
          class="rounded bg-green-500 px-4 py-2 text-white"
          disabled={!userData.consent_to_data_processing}
        >
          Сохранить
        </button>
      </div>
    </div>
  </form>