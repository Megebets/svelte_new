<script>
	import Header from '../components/Header.svelte';
	import { onMount, tick } from 'svelte';
	import { userStore, tokenStore } from '$lib/stores'; // Добавляем tokenStore
	import { get } from 'svelte/store'; // Добавляем get
	import IMask from 'imask';
  
	let isEditing = false;
	let originalData = {};
	let profileCompletion = 0;
	let phoneInput;
	let trustedPhoneInput;
  
	let userData = $userStore || {
	  avatar: '',
	  last_name: '',
	  name: '',
	  nationality: '',
	  middle_name: '',
	  pol: '',
	  has_parents: false,
	  livingplace: false,
	  birthdate: '',
	  birthplace: '',
	  residence: '',
	  contact_phone: '',
	  trusted_person_phone: '',
	  education: false,
	  education_level: '',
	  specialty: '',
	  has_working: false,
	  has_housing: false,
	  was_married: false,
	  has_children: false,
	  children_boys: 0,
	  children_girls: 0,
	  children_ages: '',
	  height: 170,
	  has_criminal_record: false,
	  has_bad_habits: '',
	  performs_namaz: false,
	  clothing_preference: '',
	  spouse_nationality_importance: false,
	  spouse_age_preference: 30,
	  ok_with_divorced_spouse: false,
	  ok_with_spouse_children: false,
	  clothing_preferences: '',
	  health: '',
	  willing_to_relocate: false,
	  agree_to_be_second_wife: false,
	  plan_to_have_children: true,
	  health_status: '',
	  additional_info: '',
	  spouse_age: '',
	  spouse_requirements: '',
	  profile_completion_date: '',
	  consent_to_data_processing: false,
	  madhhab: ''
	};
  
	function startEditing() {
	  originalData = { ...userData };
	  isEditing = true;
	}
  
	function cancelEditing() {
	  userData = { ...originalData };
	  isEditing = false;
	}
  
	async function saveProfile() {
	  if (!validateForm()) return;
  
	  try {
		const token = get(tokenStore); // Получаем токен из tokenStore
		const response = await fetch('http://localhost:8000/api/profile/', {
		  method: 'PUT',
		  headers: {
			'Content-Type': 'application/json',
			'Authorization': `Bearer ${token}` // Добавляем токен
		  },
		  body: JSON.stringify(userData)
		});
  
		if (!response.ok) {
		  const errorText = await response.text();
		  throw new Error(`Ошибка при сохранении данных: ${response.status} - ${errorText}`);
		}
  
		const data = await response.json();
		console.log('Данные успешно сохранены:', data);
		isEditing = false;
		calculateCompletion();
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
  
	function validateForm() {
	  if (!userData.name) {
		alert('Пожалуйста, укажите имя');
		return false;
	  }
	  const cleanedPhone = userData.contact_phone.replace(/\D/g, '');
	  if (!/^\d{11}$/.test(cleanedPhone) || !cleanedPhone.startsWith('7')) {
		alert('Введите корректный номер телефона (11 цифр, начиная с +7)');
		return false;
	  }
	  return true;
	}
  
	onMount(async () => {
	  calculateCompletion();
	  await tick(); // Ждём рендеринг DOM
	  if (phoneInput) {
		IMask(phoneInput, {
		  mask: '+7(000)000-00-00',
		  lazy: false,
		  placeholderChar: '_'
		});
	  }
	  if (trustedPhoneInput) {
		IMask(trustedPhoneInput, {
		  mask: '+7(000)000-00-00',
		  lazy: false,
		  placeholderChar: '_'
		});
	  }
	});
  
	$: if (!userData.has_children) {
	  userData.children_boys = 0;
	  userData.children_girls = 0;
	  userData.children_ages = '';
	}
  </script>

<div class="flex min-h-screen flex-col bg-gray-100">
	
	<div class="container mx-auto flex items-center justify-between px-4 py-4">
		<div class="flex items-center gap-4">
			<div class="rounded-full bg-gray-300">
				<img
				src={userData.avatar || '/images/avatar.jpg'}
				alt="Аватар"
				class="h-16 w-16 rounded-full object-cover"
				/>
			</div>
			<div>
				<h1 class="text-2xl font-bold">{userData.name || 'Не указано'}</h1>
				<p class="text-sm text-gray-500">Ваш личный кабинет</p>
			</div>
		</div>
		<button class="rounded bg-red-500 px-4 py-2 text-white">Выход</button>
	</div>

	<main class="container mx-auto grid flex-grow grid-cols-1 gap-8 px-4 py-8 md:grid-cols-3">
		<div class="col-span-2 rounded-lg bg-white p-6 shadow">
			<h2 class="mb-4 text-xl font-bold">Анкета</h2>

			{#if isEditing}
				<form class="mx-auto max-w-2xl rounded-md bg-white p-6 shadow-md" on:submit|preventDefault={saveProfile}>
					<h2 class="mb-4 text-xl font-semibold">Анкета пользователя</h2>

					<div class="grid grid-cols-1 gap-4">
						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Фамилия</label>
							<input
								type="text"
								bind:value={userData.last_name}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Имя</label>
							<input
								type="text"
								bind:value={userData.name}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Отчество</label>
							<input
								type="text"
								bind:value={userData.middle_name}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
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

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Дата рождения</label>
							<input
								type="date"
								bind:value={userData.birthdate}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Место рождения</label>
							<input
								type="text"
								bind:value={userData.birthplace}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Национальность</label>
							<input
								type="text"
								bind:value={userData.nationality}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Адрес проживания</label>
							<input
								type="text"
								bind:value={userData.residence}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>
						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Контактный телефон</label>
							<input
								bind:this={phoneInput}
								bind:value={userData.contact_phone}
								class="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
								placeholder="+7(999)999-99-99"
								required
							/>
						</div>
						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Телефон доверенного лица</label>
							<input
								bind:this={trustedPhoneInput}
								bind:value={userData.trusted_person_phone}
								class="mt-1 block w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
								placeholder="+7(999)999-99-99"
							/>
						</div>
						

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Рост (см)</label>
							<input
								type="number"
								bind:value={userData.height}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
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

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
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

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">У вас есть собственное жилье?</label>
							<select
								bind:value={userData.has_housing}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Есть</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
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

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Вы работаете?</label>
							<select
								bind:value={userData.has_working}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Не работаю</option>
								<option value={true}>Работаю</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Вы состояли в браке?</label>
							<select
								bind:value={userData.was_married}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Да</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">У вас есть судимость?</label>
							<select
								bind:value={userData.has_criminal_record}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Есть</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Вы совершаете намаз?</label>
							<select
								bind:value={userData.performs_namaz}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Да</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
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

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Какие вредные привычки присущи вам?</label>
							<input
								type="text"
								bind:value={userData.has_bad_habits}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Возможен брак с разведённым(ой)?</label>
							<select
								bind:value={userData.ok_with_divorced_spouse}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Да</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Возможен ли брак с человеком, у которого есть дети?</label>
							<select
								bind:value={userData.ok_with_spouse_children}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Да</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
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
							<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
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

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Планируете детей?</label>
							<select
								bind:value={userData.plan_to_have_children}
								class="mt-1 block w-full rounded-md border-gray-300"
							>
								<option value={false}>Нет</option>
								<option value={true}>Да</option>
							</select>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Ваши предпочтения в одежде:</label>
							<input
								type="text"
								bind:value={userData.clothing_preferences}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Возраст будущего(ей) супруга(и)?</label>
							<input
								type="text"
								bind:value={userData.spouse_age}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group rounded-lg border-2 border-gray-300 p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">Состояние вашего здоровья:</label>
							<input
								type="text"
								bind:value={userData.health}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							/>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
							<label class="block text-sm font-medium text-gray-700">О себе</label>
							<textarea
								bind:value={userData.additional_info}
								class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
							></textarea>
						</div>

						<div class="group border-2 border-gray-300 rounded-lg p-4 transition focus-within:border-blue-500">
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

						<div class="mt-6 flex justify-between gap-4">
							<button type="button" class="rounded bg-gray-500 px-4 py-2 text-white" on:click={cancelEditing}>
								Отмена
							</button>
							<button type="submit" class="rounded bg-green-500 px-4 py-2 text-white">
								Сохранить
							</button>
						</div>
					</div>
				</form>
			{:else}
				<p class="mb-4 text-gray-700">{userData.name || 'Имя не указано'}</p>
				<button class="rounded bg-blue-500 px-4 py-2 text-white" on:click={startEditing}>
					Редактировать анкету
				</button>
			{/if}

			<div class="mt-6">
				<h2 class="mb-4 text-xl font-bold">Заполнение анкеты</h2>
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
		</div>

		<div class="rounded-lg bg-white p-6 shadow">
			<h2 class="mb-4 text-xl font-bold">Другие анкеты</h2>
			<div class="h-64 overflow-y-auto">
				<p class="mb-2 text-gray-700">Анкета 1</p>
				<p class="mb-2 text-gray-700">Анкета 2</p>
				<p class="mb-2 text-gray-700">Анкета 3</p>
			</div>
		</div>
	</main>

	<div class="container mx-auto px-4 py-8">
		<div class="rounded-lg bg-white p-6 shadow">
			<div class="h-64 overflow-y-auto">
				<h2 class="mb-4 text-xl font-bold">Полезные советы</h2>
				<p class="mb-2 text-gray-700">Будь мягок со своей семьей</p>
			</div>
		</div>
	</div>
</div>