<script>
	import { onMount } from 'svelte';
	import { userStore, tokenStore } from '$lib/stores';
	import ProfileInfo from './ProfileInfo.svelte';
	import UsefulTips from './UsefulTips.svelte';
	import OtherProfiles from './OtherProfiles.svelte';
  
	let isEditing = false;
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
	  spouse_age_min: 18,
	  spouse_age_max: 30,
	  ok_with_divorced_spouse: false,
	  ok_with_spouse_children: false,
	  clothing_preferences: '',
	  health: '',
	  willing_to_relocate: false,
	  agree_to_be_second_wife: false,
	  plan_to_have_children: true,
	  health_status: '',
	  additional_info: '',
	  spouse_requirements: '',
	  profile_completion_date: '',
	  consent_to_data_processing: false,
	  madhhab: '',
	  is_approved: false
	};
	let tipsData = [];
	let profilesData = [];
  
	function startEditing() {
	  isEditing = true;
	}
  
	function cancelEditing() {
	  isEditing = false;
	}
  
	function logout() {
	  tokenStore.set(null);
	  userStore.set(null);
	  window.location.href = '/login';
	}
  
	function handleSave(updatedData) {
	  userData = updatedData;
	  userStore.set(updatedData);
	  isEditing = false;
	}
  
	async function fetchTips() {
	  try {
		const response = await fetch('http://localhost:8000/api/tips/', {
		  headers: { 'Authorization': `Bearer ${$tokenStore}` }
		});
		if (response.ok) {
		  tipsData = await response.json();
		}
	  } catch (error) {
		console.error('Ошибка загрузки советов:', error);
	  }
	}
  
	async function fetchProfiles() {
	  try {
		const response = await fetch('http://localhost:8000/api/profiles/', {
		  headers: { 'Authorization': `Bearer ${$tokenStore}` }
		});
		if (response.ok) {
		  profilesData = await response.json();
		}
	  } catch (error) {
		console.error('Ошибка загрузки анкет:', error);
	  }
	}
  
	onMount(() => {
	  fetchTips();
	  fetchProfiles();
	});
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

	  <button class="rounded bg-red-500 px-4 py-2 text-white" on:click={logout}>Выход</button>
	</div>
  
	<main class="flex flex-col w-3/4 mx-auto gap-8 px-4 py-8 {isEditing ? 'md:flex-row' : ''}">
		<div class="rounded-lg bg-white p-6 shadow w-full {isEditing ? 'md:w-1/2' : ''}">
		  {#if !isEditing}
			<button class="rounded bg-blue-500 px-4 py-2 text-white" on:click={startEditing}>
			  Редактировать анкету
			</button>
		  {/if}
		  {#if isEditing}
			<ProfileInfo userData={userData} onSave={handleSave} onCancel={cancelEditing} />
		  {/if}
		</div>
	  
		<div class="rounded-lg bg-white p-6 shadow w-full {isEditing ? 'md:w-1/2' : ''}">
		  <UsefulTips tips={tipsData} />
		  <OtherProfiles profiles={profilesData} />
		</div>
	</main>
  </div>