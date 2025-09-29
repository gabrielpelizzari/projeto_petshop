<template>
  <div class="space-y-8">
    <!-- Header Section -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Gerenciamento de Raças</h1>
        <p class="mt-2 text-gray-600">Controle completo das raças cadastradas</p>
      </div>
      <button
        @click="showAddRacaModal = true"
        class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
      >
        <span class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
          </svg>
          <span>Nova Raça</span>
        </span>
      </button>
    </div>

    <!-- Main Content -->
    <div class="bg-white/60 backdrop-blur-sm rounded-2xl border border-gray-100 shadow-lg overflow-hidden">
      <div class="p-6 border-b border-gray-200/50">
        <h2 class="text-xl font-semibold text-gray-900">Raças Cadastradas</h2>
        <p class="text-sm text-gray-600 mt-1">{{ racas.length }} raça(s) registrada(s)</p>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="bg-gradient-to-r from-gray-50 to-gray-100">
            <tr>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">ID</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Nome da Raça</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Pets Cadastrados</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Ações</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="(raca, index) in racas"
              :key="raca.id"
              class="hover:bg-gray-50/50 transition-colors duration-200"
            >
              <td class="py-4 px-6 text-sm font-medium text-gray-900">{{ raca.id }}</td>
              <td class="py-4 px-6 text-sm text-gray-900 font-medium">{{ raca.nome }}</td>
              <td class="py-4 px-6 text-sm text-gray-600">{{ getPetsCount(raca.id) }} pet(s)</td>
              <td class="py-4 px-6 text-sm">
                <div class="flex space-x-2">
                  <button
                    @click="startEdit(raca)"
                    class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-100 rounded-lg hover:bg-blue-200 transition-colors duration-200"
                  >
                    Editar
                  </button>
                  <button
                    @click="handleDeleteRaca(raca.id, raca.nome)"
                    class="px-3 py-1.5 text-xs font-medium text-red-700 bg-red-100 rounded-lg hover:bg-red-200 transition-colors duration-200"
                  >
                    Excluir
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Empty State -->
        <div v-if="racas.length === 0 && !loading" class="text-center py-12">
          <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"/>
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">Nenhuma raça cadastrada</h3>
          <p class="mt-1 text-sm text-gray-500">Comece criando uma nova raça para seus pets.</p>
        </div>
      </div>
    </div>

    <!-- Add Raca Modal -->
    <div v-if="showAddRacaModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50">
      <div class="bg-white rounded-2xl p-8 max-w-md w-full mx-4 shadow-2xl">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-semibold text-gray-900">Nova Raça</h3>
          <button @click="showAddRacaModal = false" class="text-gray-400 hover:text-gray-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
        
        <form @submit.prevent="handleCreateRaca" class="space-y-6">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Nome da Raça *</label>
            <input 
              type="text" 
              v-model="newRaca.nome" 
              required 
              placeholder="Ex: Labrador, Poodle, Siamês..."
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
            >
          </div>
          
          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button" 
              @click="showAddRacaModal = false" 
              class="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
            >
              Criar Raça
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Edit Raca Modal -->
    <div v-if="editingRacaId" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50">
      <div class="bg-white rounded-2xl p-8 max-w-md w-full mx-4 shadow-2xl">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-semibold text-gray-900">Editar Raça</h3>
          <button @click="editingRacaId = null" class="text-gray-400 hover:text-gray-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
        
        <form @submit.prevent="handleUpdateRaca" class="space-y-6">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Nome da Raça *</label>
            <input 
              type="text" 
              v-model="editableRacaData.nome" 
              required 
              placeholder="Ex: Labrador, Poodle, Siamês..."
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
            >
          </div>
          
          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button" 
              @click="editingRacaId = null" 
              class="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
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
import { ref, onMounted } from 'vue';
import api from '@/services/api';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';

const racas = ref([]);
const pets = ref([]);
const loading = ref(true);
const error = ref(null);

const showAddRacaModal = ref(false);
const editingRacaId = ref(null);

const newRaca = ref({ nome: '' });
const editableRacaData = ref({ id: null, nome: '' });

const { showSuccess, successUpdate, successDelete } = useSuccessMessage();
const { showApiError } = useErrorMessage();
const { confirmDelete } = useConfirmation();


const fetchData = async () => {
  loading.value = true;
  error.value = null;
  try {
    const [racasRes, petsRes] = await Promise.all([
      api.get('/racas'),
      api.get('/pets')
    ]);
    racas.value = racasRes.data;
    pets.value = petsRes.data;
  } catch (err) {
    console.error('Erro ao buscar dados de raças:', err);
    showApiError(err);
    error.value = err;
  } finally {
    loading.value = false;
  }
};

// Conta quantos pets existem para uma raça específica.
const getPetsCount = (racaId) => {
  return pets.value.filter(pet => pet.raca_id === racaId).length;
};


const handleCreateRaca = async () => {
  if (!newRaca.value.nome.trim()) {
    return;
  }

  try {
    await api.post('/racas', newRaca.value);
    showSuccess('Raça criada com sucesso!');
    
    // Reset form
    newRaca.value = { nome: '' };
    showAddRacaModal.value = false;
    
    // Refresh data
    await fetchData();
  } catch (err) {
    console.error('Erro ao criar raça:', err);
    showApiError(err);
  }
};


const startEdit = (raca) => {
  editableRacaData.value = { ...raca };
  editingRacaId.value = raca.id;
};


const handleUpdateRaca = async () => {
  if (!editableRacaData.value.nome.trim()) {
    return;
  }

  try {
    await api.put(`/racas/${editableRacaData.value.id}`, {
      nome: editableRacaData.value.nome
    });
    
    successUpdate('Raça');
    editingRacaId.value = null;
    
    // Refresh data
    await fetchData();
  } catch (err) {
    console.error('Erro ao atualizar raça:', err);
    showApiError(err);
  }
};



const handleDeleteRaca = async (racaId, racaNome) => {
  // Verifica se há pets usando esta raça
  const petsCount = getPetsCount(racaId);
  
  if (petsCount > 0) {
    showApiError({
      response: {
        data: {
          detail: `Não é possível excluir a raça "${racaNome}" pois existem ${petsCount} pet(s) cadastrado(s) com esta raça.`
        }
      }
    });
    return;
  }

  const confirmed = await confirmDelete(
    `a raça "${racaNome}"`,
    'Esta ação não pode ser desfeita.'
  );

  if (!confirmed) return;

  try {
    await api.delete(`/racas/${racaId}`);
    successDelete('Raça');
    
    // Refresh data
    await fetchData();
  } catch (err) {
    console.error('Erro ao excluir raça:', err);
    showApiError(err);
  }
};

onMounted(() => {
  fetchData();
});
</script>