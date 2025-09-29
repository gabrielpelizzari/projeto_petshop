<template>
  <div class="space-y-8">
    <!-- Header Section -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Gerenciamento de Pets</h1>
        <p class="mt-2 text-gray-600">Controle completo dos pets cadastrados</p>
      </div>
      <button
        @click="showAddPetModal = true"
        class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
      >
        <span class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
          </svg>
          <span>Novo Pet</span>
        </span>
      </button>
    </div>

    <!-- Main Content -->
    <div class="bg-white/60 backdrop-blur-sm rounded-2xl border border-gray-100 shadow-lg overflow-hidden">
      <div class="p-6 border-b border-gray-200/50">
        <h2 class="text-xl font-semibold text-gray-900">Pets Cadastrados</h2>
        <p class="text-sm text-gray-600 mt-1">{{ pets.length }} pet(s) registrado(s)</p>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="bg-gradient-to-r from-gray-50 to-gray-100">
            <tr>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">ID</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Nome do Pet</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Raça</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Dono</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Ações</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="(pet, index) in pets"
              :key="pet.id"
              class="hover:bg-gray-50/50 transition-colors duration-200"
            >
              <td class="py-4 px-6 text-sm font-medium text-gray-900">{{ pet.id }}</td>
              <td class="py-4 px-6 text-sm text-gray-900 font-medium">{{ pet.nome }}</td>
              <td class="py-4 px-6 text-sm text-gray-600">{{ getRacaNome(pet.raca_id) }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ getClienteNome(pet.cliente_id) }}</td>
              <td class="py-4 px-6 text-sm">
                <div class="flex space-x-2">
                  <button
                    @click="openEditPetModal(pet)"
                    class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-100 rounded-lg hover:bg-blue-200 transition-colors duration-200"
                  >
                    Editar
                  </button>
                  <button
                    @click="handleDeletePet(pet.id)"
                    class="px-3 py-1.5 text-xs font-medium text-red-700 bg-red-100 rounded-lg hover:bg-red-200 transition-colors duration-200"
                  >
                    Excluir
                  </button>
                </div>
              </td>
            </tr>
            <tr v-if="pets.length === 0">
              <td colspan="5" class="py-12 text-center">
                <div class="flex flex-col items-center space-y-3">
                  <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                  </svg>
                  <p class="text-gray-500 font-medium">Nenhum pet cadastrado</p>
                  <p class="text-gray-400 text-sm">Clique em "Novo Pet" para começar</p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal de Adicionar Pet -->
    <div v-if="showAddPetModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm overflow-y-auto h-full w-full flex items-center justify-center p-4 z-50">
      <div class="bg-white/90 backdrop-blur-md rounded-2xl p-8 w-full max-w-lg shadow-2xl border border-gray-200">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-gray-900">Novo Pet</h3>
          <button
            @click="cancelAddPet"
            class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
        <form @submit.prevent="handleCreatePet" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Nome do Pet</label>
              <input 
                type="text" 
                v-model="newPet.nome" 
                required 
                placeholder="Digite o nome do pet"
                class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Data de Nascimento *</label>
              <input 
                type="date" 
                v-model="newPet.data_nascimento" 
                :max="maxDate"
                :class="[
                  'w-full px-4 py-3 bg-white/80 border rounded-xl focus:outline-none focus:ring-2 transition-all duration-200',
                  dateValidationClass
                ]"
              >
              <!-- Mensagem de validação da data -->
              <div v-if="showDateValidation" class="mt-2 text-sm flex items-center space-x-2">
                <svg v-if="isDateValid" class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <svg v-else class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span :class="isDateValid ? 'text-green-600' : 'text-red-600'">
                  {{ getDateValidationMessage() }}
                </span>
              </div>
            </div>
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Dono</label>
            <select 
              v-model="newPet.cliente_id" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
            >
              <option disabled value="">Selecione o dono</option>
              <option v-for="cliente in clientes" :key="cliente.id" :value="cliente.id">{{ cliente.nome }}</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Raça</label>
            <select 
              v-model="newPet.raca_id" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
            >
              <option disabled value="">Selecione a raça</option>
              <option v-for="raca in racas" :key="raca.id" :value="raca.id">{{ raca.nome }}</option>
            </select>
          </div>
          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button" 
              @click="cancelAddPet" 
              class="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              :disabled="!isFormValid"
              class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            >
              Salvar Pet
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal de Editar Pet -->
    <div v-if="editingPetId" class="fixed inset-0 bg-black/50 backdrop-blur-sm overflow-y-auto h-full w-full flex items-center justify-center p-4 z-50">
      <div class="bg-white/90 backdrop-blur-md rounded-2xl p-8 w-full max-w-lg shadow-2xl border border-gray-200">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-gray-900">Editar Pet</h3>
          <button
            @click="cancelEditPet"
            class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
        <form @submit.prevent="handleUpdatePet" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Nome do Pet</label>
              <input 
                type="text" 
                v-model="editablePetData.nome" 
                required 
                class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Data de Nascimento *</label>
              <input 
                type="date" 
                v-model="editablePetData.data_nascimento" 
                :max="maxDate"
                :class="[
                  'w-full px-4 py-3 bg-white/80 border rounded-xl focus:outline-none focus:ring-2 transition-all duration-200',
                  editDateValidationClass
                ]"
              >
              <!-- Mensagem de validação da data -->
              <div v-if="showEditDateValidation" class="mt-2 text-sm flex items-center space-x-2">
                <svg v-if="isEditDateValid" class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <svg v-else class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span :class="isEditDateValid ? 'text-green-600' : 'text-red-600'">
                  {{ getEditDateValidationMessage() }}
                </span>
              </div>
            </div>
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Dono</label>
            <select 
              v-model="editablePetData.cliente_id" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
            >
              <option v-for="cliente in clientes" :key="cliente.id" :value="cliente.id">{{ cliente.nome }}</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Raça</label>
            <select 
              v-model="editablePetData.raca_id" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
            >
              <option v-for="raca in racas" :key="raca.id" :value="raca.id">{{ raca.nome }}</option>
            </select>
          </div>
          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button" 
              @click="cancelEditPet" 
              class="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              :disabled="!isEditFormValid"
              class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            >
              Salvar Alterações
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import api from '@/services/api';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';

const pets = ref([]);
const clientes = ref([]);
const racas = ref([]);
const loading = ref(true);
const error = ref(null);

const showAddPetModal = ref(false);
const editingPetId = ref(null);

const newPet = ref({ nome: '', data_nascimento: '', raca_id: null, cliente_id: null });
const editablePetData = ref({ id: null, nome: '', data_nascimento: '', raca_id: null, cliente_id: null });

const { showSuccess, successUpdate, successDelete } = useSuccessMessage();
const { showApiError, showError } = useErrorMessage();
const { confirmDelete } = useConfirmation();

// ===== VALIDAÇÕES DE DATA =====

// Data máxima permitida (hoje)
const maxDate = computed(() => {
  const today = new Date();
  return today.toISOString().split('T')[0];
});

// Validações para o formulário de criação
const isDateValid = computed(() => {
  if (!newPet.value.data_nascimento || newPet.value.data_nascimento.trim() === '') {
    return false;
  }
  const [ano, mes, dia] = newPet.value.data_nascimento.split('-').map(Number);
  const selectedDate = new Date(ano, mes - 1, dia);
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  return selectedDate <= today;
});

const showDateValidation = computed(() => {
  return true;
});

const dateValidationClass = computed(() => {
  if (!showDateValidation.value) {
    return 'border-gray-200 focus:border-green-500 focus:ring-green-500/20';
  }
  
  return isDateValid.value 
    ? 'border-green-300 focus:border-green-500 focus:ring-green-500/20'
    : 'border-red-300 focus:border-red-500 focus:ring-red-500/20';
});

const isFormValid = computed(() => {
  return newPet.value.nome.trim() && newPet.value.raca_id && newPet.value.cliente_id && isDateValid.value;
});

// Validações para o formulário de edição
const isEditDateValid = computed(() => {
  if (!editablePetData.value.data_nascimento || editablePetData.value.data_nascimento.trim() === '') {
    return false;
  }
  const [ano, mes, dia] = editablePetData.value.data_nascimento.split('-').map(Number);
  const selectedDate = new Date(ano, mes - 1, dia);
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  return selectedDate <= today;
});

const showEditDateValidation = computed(() => {
  return true;
});

const editDateValidationClass = computed(() => {
  if (!showEditDateValidation.value) {
    return 'border-gray-200 focus:border-green-500 focus:ring-green-500/20';
  }
  
  return isEditDateValid.value 
    ? 'border-green-300 focus:border-green-500 focus:ring-green-500/20'
    : 'border-red-300 focus:border-red-500 focus:ring-red-500/20';
});

const isEditFormValid = computed(() => {
  return editablePetData.value.nome.trim() && editablePetData.value.raca_id && editablePetData.value.cliente_id && isEditDateValid.value;
});

// Funções de mensagens de validação
const getDateValidationMessage = () => {
  if (!newPet.value.data_nascimento || newPet.value.data_nascimento.trim() === '') {
    return 'A data de nascimento é obrigatória';
  }
  
  const [ano, mes, dia] = newPet.value.data_nascimento.split('-').map(Number);
  const selectedDate = new Date(ano, mes - 1, dia);
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  
  if (selectedDate > today) {
    return 'A data de nascimento não pode ser uma data futura';
  }
  
  return 'Data válida';
};

const getEditDateValidationMessage = () => {
  if (!editablePetData.value.data_nascimento || editablePetData.value.data_nascimento.trim() === '') {
    return 'A data de nascimento é obrigatória';
  }
  
  const [ano, mes, dia] = editablePetData.value.data_nascimento.split('-').map(Number);
  const selectedDate = new Date(ano, mes - 1, dia);
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  
  if (selectedDate > today) {
    return 'A data de nascimento não pode ser uma data futura';
  }
  
  return 'Data válida';
};

const fetchData = async () => {
  loading.value = true;
  error.value = null;
  try {
    const [petsRes, clientesRes, racasRes] = await Promise.all([
      api.get('/pets'),
      api.get('/clientes'),
      api.get('/racas')
    ]);
    pets.value = petsRes.data;
    clientes.value = clientesRes.data;
    racas.value = racasRes.data;
  } catch (err) {
    console.error('Erro ao buscar dados de pets:', err);
    showApiError(err);
    error.value = err;
  } finally {
    loading.value = false;
  }
};

const getClienteNome = (clienteId) => {
  const cliente = clientes.value.find(c => c.id === clienteId);
  return cliente ? cliente.nome : 'N/A';
};

const getRacaNome = (racaId) => {
  const raca = racas.value.find(r => r.id === racaId);
  return raca ? raca.nome : 'N/A';
};

const handleCreatePet = async () => {
  if (!newPet.value.nome.trim()) {
    showError('O nome do pet é obrigatório.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!newPet.value.raca_id) {
    showError('A raça do pet é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!newPet.value.cliente_id) {
    showError('É obrigatório selecionar um dono para o pet.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!newPet.value.data_nascimento || newPet.value.data_nascimento.trim() === '') {
    showError('A data de nascimento é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!isDateValid.value) {
    showError('A data de nascimento não pode ser no futuro.', { title: 'Data Inválida' });
    return;
  }

  try {
    await api.post(`/clientes/${newPet.value.cliente_id}/pets`, newPet.value);
    showSuccess('Pet criado com sucesso!');
    cancelAddPet(); // Limpa os campos e fecha o modal
    fetchData();
  } catch (err) {
    console.error('Erro ao criar pet:', err);
    showApiError(err);
  }
};

const openEditPetModal = (pet) => {
  editingPetId.value = pet.id;
  editablePetData.value = { ...pet };
};

const handleUpdatePet = async () => {
  if (!editingPetId.value) return;
  
  if (!editablePetData.value.nome.trim()) {
    showError('O nome do pet é obrigatório.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!editablePetData.value.raca_id) {
    showError('A raça do pet é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!editablePetData.value.cliente_id) {
    showError('É obrigatório selecionar um dono para o pet.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!editablePetData.value.data_nascimento || editablePetData.value.data_nascimento.trim() === '') {
    showError('A data de nascimento é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!isEditDateValid.value) {
    showError('A data de nascimento não pode ser no futuro.', { title: 'Data Inválida' });
    return;
  }

  try {
    await api.put(`/pets/${editingPetId.value}`, editablePetData.value);
    successUpdate('Pet');
    cancelEditPet(); // Limpa os campos e fecha o modal
    fetchData();
  } catch (err) {
    console.error('Erro ao atualizar pet:', err);
    showApiError(err, 'Não foi possível atualizar o pet.');
  }
};

const handleDeletePet = async (petId) => {
  const confirmed = await confirmDelete('este pet');
  
  if (!confirmed) return;
  
  try {
    await api.delete(`/pets/${petId}`);
    successDelete('Pet');
    fetchData();
  } catch (err) {
    console.error('Erro ao excluir pet:', err);
    showApiError(err, 'Não foi possível excluir o pet.');
  }
};

const cancelAddPet = () => {
  showAddPetModal.value = false;
  newPet.value = { nome: '', data_nascimento: '', raca_id: null, cliente_id: null };
};

const cancelEditPet = () => {
  editingPetId.value = null;
  editablePetData.value = { id: null, nome: '', data_nascimento: '', raca_id: null, cliente_id: null };
};



onMounted(() => {
  fetchData();
});
</script>
