<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo e Título -->
          <div class="flex items-center space-x-4">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
              <h1 class="text-xl font-semibold text-gray-900">PetHub</h1>
            </div>
          </div>

          <!-- User Info e Logout -->
          <div class="flex items-center space-x-4">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
              <div class="hidden md:block">
                <p class="text-sm font-medium text-gray-900">{{ cliente?.nome?.split(' ')[0] || 'Cliente' }}</p>
                <p class="text-xs text-gray-500">Área do Cliente</p>
              </div>
            </div>
            <button 
              @click="handleLogout"
              class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors duration-200"
              title="Sair da conta"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Loading State -->
      <div v-if="loading" class="flex items-center justify-center py-12">
        <div class="flex items-center space-x-3">
          <svg class="animate-spin w-6 h-6 text-blue-600" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <p class="text-gray-600 font-medium">Carregando seus dados...</p>
        </div>
      </div>

      <!-- Error State -->
      <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-6">
        <div class="flex items-center space-x-3">
          <svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <div>
            <p class="text-red-800 font-medium">Erro ao carregar dados</p>
            <p class="text-red-600 text-sm mt-1">{{ error.message }}</p>
          </div>
        </div>
      </div>

      <!-- Dashboard Content -->
      <div v-if="!loading && !error" class="space-y-8">
        <!-- Welcome Section -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-2xl font-bold text-gray-900">Olá, {{ cliente?.nome?.split(' ')[0] || 'Cliente' }}! 👋</h2>
              <p class="text-gray-600 mt-1">Bem-vindo ao seu painel de controle</p>
            </div>
            <button 
              @click="showEditProfile = true"
              class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors duration-200 flex items-center space-x-2"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
              <span>Meu Perfil</span>
            </button>
          </div>
        </div>

        <!-- Stats Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
              <div class="ml-4">
                <p class="text-sm font-medium text-gray-600">Total de Pets</p>
                <p class="text-2xl font-bold text-gray-900">{{ pets.length }}</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <div class="ml-4">
                <p class="text-sm font-medium text-gray-600">Atendimentos</p>
                <p class="text-2xl font-bold text-gray-900">{{ totalAtendimentos }}</p>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
            <div class="flex items-center">
              <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                </svg>
              </div>
              <div class="ml-4">
                <p class="text-sm font-medium text-gray-600">Valor Total</p>
                <p class="text-2xl font-bold text-gray-900">R$ {{ valorTotalAtendimentos.toFixed(2) }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Pets Section -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200">
          <div class="px-6 py-4 border-b border-gray-200">
            <div class="flex items-center justify-between">
              <h3 class="text-lg font-semibold text-gray-900">Meus Pets</h3>
              <button 
                v-if="!showAddPetForm"
                @click="showAddPetForm = true"
                class="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors duration-200 flex items-center space-x-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                </svg>
                <span>Adicionar Pet</span>
              </button>
            </div>
          </div>

          <div class="p-6">
            <!-- Add Pet Form -->
            <AddPetForm 
              v-if="showAddPetForm"
              :racas="racas"
              @add-pet="handleAddPet"
              @close="showAddPetForm = false"
              class="mb-6"
            />

            <!-- Pets Grid -->
            <div v-if="pets.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <PetCard 
                v-for="pet in pets"
                :key="pet.id"
                :pet="pet"
                :racas="racas"
                @update-pet="handleUpdatePet"
                @delete-pet="handleDeletePet"
              />
            </div>

            <!-- Empty State -->
            <div v-else class="text-center py-12">
              <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
              <h3 class="text-lg font-medium text-gray-900 mb-2">Nenhum pet cadastrado</h3>
              <p class="text-gray-600 mb-4">Que tal adicionar seu primeiro companheiro?</p>
              <button 
                @click="showAddPetForm = true"
                class="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors duration-200"
              >
                Adicionar Primeiro Pet
              </button>
            </div>
          </div>
        </div>

      </div>
    </main>

    <!-- Modal Elegante para Meu Perfil -->
    <div v-if="showEditProfile" class="fixed inset-0 z-50 overflow-y-auto">
      <!-- Backdrop com blur sutil -->
      <div class="fixed inset-0 bg-gray-500/20 backdrop-blur-sm transition-opacity" @click="showEditProfile = false"></div>
      
      <!-- Modal Container -->
      <div class="flex min-h-full items-center justify-center p-4">
        <div class="relative bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden transform transition-all">
          <!-- Header do Modal -->
          <div class="bg-gradient-to-r from-blue-600 to-purple-600 px-6 py-4">
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                  </svg>
                </div>
                <div>
                  <h3 class="text-xl font-semibold text-white">Meu Perfil</h3>
                  <p class="text-blue-100 text-sm">Gerencie suas informações pessoais</p>
                </div>
              </div>
              <button 
                @click="showEditProfile = false"
                class="p-2 text-white/80 hover:text-white hover:bg-white/10 rounded-lg transition-colors duration-200"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Conteúdo do Modal -->
          <div class="p-6 max-h-[calc(90vh-120px)] overflow-y-auto">
            <ClientProfile 
              :cliente="cliente"
              @update-profile="handleUpdateClienteModal"
              @change-password="handleChangePassword"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import api from '@/services/api';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';

// Importar componentes
import ClientProfile from '../components/ClientProfile.vue';
import PetCard from '../components/PetCard.vue';
import AddPetForm from '../components/AddPetForm.vue';

// Composables
const { successCreate, successUpdate, successDelete } = useSuccessMessage();
const { showApiError } = useErrorMessage();
const { confirmDelete, confirmLogout } = useConfirmation();

const router = useRouter();
const authStore = useAuthStore();

const cliente = ref(null);
const pets = ref([]);
const racas = ref([]);

const showAddPetForm = ref(false);
const showEditProfile = ref(false);
const loading = ref(true);
const error = ref(null);

const totalAtendimentos = computed(() => {
  return pets.value.reduce((total, pet) => total + (pet.atendimentos?.length || 0), 0);
});

const valorTotalAtendimentos = computed(() => {
  return pets.value.reduce((total, pet) => {
    return total + (pet.atendimentos?.reduce((petTotal, atendimento) => petTotal + (atendimento.valor || 0), 0) || 0);
  }, 0);
});

const fetchData = async () => {
  loading.value = true;
  error.value = null;
  try {
    const [clienteResponse, petsResponse, racasResponse] = await Promise.all([
      api.get('/clientes/me'),
      api.get('/clientes/me/pets'),
      api.get('/racas') 
    ]);

    cliente.value = clienteResponse.data;
    const petsData = petsResponse.data;
    racas.value = racasResponse.data;

    if (petsData.length > 0) {
      const petsComAtendimentos = await Promise.all(
        petsData.map(async (pet) => {
          try {
            const atendimentosResponse = await api.get(`/pets/${pet.id}/atendimentos`);
            return { ...pet, atendimentos: atendimentosResponse.data };
          } catch (err) {
            console.error(`Falha ao buscar atendimentos para o pet ${pet.id}:`, err);
            showApiError(err, `Falha ao buscar atendimentos para o pet ${pet.id}`);
            return { ...pet, atendimentos: [] }; // Retorna o pet com atendimentos vazios em caso de erro
          }
        })
      );
      pets.value = petsComAtendimentos;
    } else {
      pets.value = petsData;
    }

  } catch (err) {
    console.error('Falha ao buscar dados do dashboard:', err);
    showApiError(err);
  } finally {
    loading.value = false;
  }
};

const handleAddPet = async (petData) => {
  try {
    const response = await api.post(`/clientes/${cliente.value.id}/pets`, petData);
    const novoPet = response.data;
    // Garante que o novo pet tenha a propriedade 'atendimentos' para evitar erros de renderização
    novoPet.atendimentos = [];
    pets.value.push(novoPet);
    showAddPetForm.value = false;
    successCreate('Pet');
  } catch (err) {
    console.error('Erro ao adicionar pet:', err);
    showApiError(err);
  }
};

const handleUpdateCliente = async (clienteData) => {
  try {
    const response = await api.put('/clientes/me', clienteData);
    cliente.value = response.data;
    successUpdate("Dados do perfil");
  } catch (err) {
    console.error('Erro ao atualizar cliente:', err);
    showApiError(err);
  }
};

const handleUpdateClienteModal = async (clienteData) => {
  try {
    const response = await api.put('/clientes/me', clienteData);
    cliente.value = response.data;
    showEditProfile.value = false;
    successUpdate("Dados do perfil");
  } catch (err) {
    console.error('Erro ao atualizar cliente:', err);
    showApiError(err);
  }
};

const handleUpdatePet = async (petData) => {
  try {
    const response = await api.put(`/pets/${petData.id}`, petData);
    const index = pets.value.findIndex(p => p.id === petData.id);
    if (index !== -1) {
      pets.value[index] = response.data;
    }
    successUpdate('Pet');
  } catch (err) {
    console.error('Erro ao atualizar pet:', err);
    showApiError(err);
  }
};

const handleChangePassword = async (passwordData) => {
  try {
    await api.put('/usuarios/me/update-password', passwordData);
    successUpdate('Senha');
  } catch (err) {
    console.error('Erro ao atualizar senha:', err);
    showApiError(err);
  }
};

const handleDeletePet = async (petId) => {
  const confirmed = await confirmDelete('este pet');
  
  if (!confirmed) return;
  
  try {
    await api.delete(`/pets/${petId}`);
    // Remove o pet da lista local para atualizar a UI instantaneamente
    pets.value = pets.value.filter(p => p.id !== petId);
    successDelete('Pet');
  } catch (err) {
    console.error('Erro ao excluir pet:', err);
    showApiError(err, 'Não foi possível excluir o pet');
  }
};

const handleLogout = async () => {
  const confirmed = await confirmLogout();
  
  if (confirmed) {
    authStore.logout();
    router.push('/');
  }
};

onMounted(() => {
  fetchData();
});
</script>
