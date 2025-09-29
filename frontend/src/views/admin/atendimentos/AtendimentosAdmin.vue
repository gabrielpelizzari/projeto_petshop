<template>
  <div class="space-y-8">
    <!-- Header Section -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Gerenciamento de Atendimentos</h1>
        <p class="mt-2 text-gray-600">Controle completo dos atendimentos realizados</p>
      </div>
      <button
        @click="openCreateModal"
        class="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white font-semibold rounded-xl hover:from-purple-700 hover:to-blue-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
      >
        <span class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
          </svg>
          <span>Novo Atendimento</span>
        </span>
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="bg-white/60 backdrop-blur-sm rounded-2xl p-8 border border-gray-100 shadow-lg">
      <div class="flex items-center justify-center space-x-3">
        <svg class="animate-spin w-6 h-6 text-purple-600" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        <p class="text-gray-600 font-medium">Carregando atendimentos...</p>
      </div>
    </div>

    <!-- Error State -->
    <div v-if="error" class="bg-red-50/80 backdrop-blur-sm rounded-2xl p-6 border border-red-200 shadow-lg">
      <div class="flex items-center space-x-3">
        <svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <div>
          <p class="text-red-800 font-medium">Erro ao carregar atendimentos</p>
          <p class="text-red-600 text-sm mt-1">{{ error.message }}</p>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div v-if="!loading && !error" class="bg-white/60 backdrop-blur-sm rounded-2xl border border-gray-100 shadow-lg overflow-hidden">
      <div class="p-6 border-b border-gray-200/50">
        <h2 class="text-xl font-semibold text-gray-900">Atendimentos Cadastrados</h2>
        <p class="text-sm text-gray-600 mt-1">{{ atendimentos.length }} atendimento(s) registrado(s)</p>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="bg-gradient-to-r from-gray-50 to-gray-100">
            <tr>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Data</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Descrição</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Valor</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Pet</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Cliente</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Ações</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="(atendimento, index) in atendimentos"
              :key="atendimento.id"
              class="hover:bg-gray-50/50 transition-colors duration-200"
            >
              <td class="py-4 px-6 text-sm text-gray-900">{{ formatarData(atendimento.data) }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ atendimento.descricao }}</td>
              <td class="py-4 px-6 text-sm font-semibold text-green-600">R$ {{ atendimento.valor.toFixed(2) }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ atendimento.pet_nome }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ atendimento.cliente_nome }}</td>
              <td class="py-4 px-6 text-sm">
                <div class="flex space-x-2">
                  <button
                    @click="openEditModal(atendimento)"
                    class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-100 rounded-lg hover:bg-blue-200 transition-colors duration-200"
                  >
                    Editar
                  </button>
                  <button
                    @click="handleDelete(atendimento.id)"
                    class="px-3 py-1.5 text-xs font-medium text-red-700 bg-red-100 rounded-lg hover:bg-red-200 transition-colors duration-200"
                  >
                    Excluir
                  </button>
                </div>
              </td>
            </tr>
            <tr v-if="atendimentos.length === 0">
              <td colspan="6" class="py-12 text-center">
                <div class="flex flex-col items-center space-y-3">
                  <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                  </svg>
                  <p class="text-gray-500 font-medium">Nenhum atendimento registrado</p>
                  <p class="text-gray-400 text-sm">Clique em "Novo Atendimento" para começar</p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal Criar -->
    <div
      v-if="showCreateModal"
      class="fixed inset-0 bg-black/50 backdrop-blur-sm overflow-y-auto h-full w-full flex items-center justify-center p-4 z-50"
    >
      <div class="bg-white/90 backdrop-blur-md rounded-2xl p-8 w-full max-w-lg shadow-2xl border border-gray-200">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-gray-900">Novo Atendimento</h3>
          <button
            @click="closeCreateModal"
            class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
        <form @submit.prevent="handleCreate" class="space-y-4">
          <div>
            <label class="block mb-1 font-bold">Pet</label>
            <select v-model="newAtendimento.pet_id" required class="w-full px-3 py-2 border rounded-md">
              <option disabled value="">Selecione um pet</option>
              <option
                v-for="pet in petOptions"
                :key="pet.id"
                :value="pet.id"
              >
                {{ pet.nome }} — {{ pet.clienteNome }}
              </option>
            </select>
          </div>
          <div>
            <label class="block mb-1 font-bold">Descrição</label>
            <input type="text" v-model="newAtendimento.descricao" required class="w-full px-3 py-2 border rounded-md">
          </div>
          <div>
            <label class="block mb-1 font-bold">Valor (R$)</label>
            <input type="number" step="0.01" v-model="newAtendimento.valor" required class="w-full px-3 py-2 border rounded-md">
          </div>
          <div>
            <label class="block mb-1 font-bold">Data</label>
            <input type="date" v-model="newAtendimento.data" required class="w-full px-3 py-2 border rounded-md">
          </div>
          <div class="flex justify-end space-x-4">
            <button type="button" @click="closeCreateModal" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300">
              Cancelar
            </button>
            <button type="submit" class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700">
              Salvar
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal Editar -->
    <div
      v-if="showEditModal"
      class="fixed inset-0 bg-black/50 backdrop-blur-sm overflow-y-auto h-full w-full flex items-center justify-center p-4 z-50"
    >
      <div class="bg-white/90 backdrop-blur-md rounded-2xl p-8 w-full max-w-lg shadow-2xl border border-gray-200">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-gray-900">Alterar Atendimento</h3>
          <button
            @click="closeEditModal"
            class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <form @submit.prevent="handleUpdate" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Pet</label>
              <input
                type="text"
                :value="getPetNome(editableAtendimento.pet_id)"
                disabled
                class="w-full px-4 py-3 bg-gray-100 border border-gray-200 rounded-xl text-gray-600"
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Dono</label>
              <input
                type="text"
                :value="editableAtendimento.cliente_nome"
                disabled
                class="w-full px-4 py-3 bg-gray-100 border border-gray-200 rounded-xl text-gray-600"
              >
            </div>
          </div>

          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Descrição</label>
            <input
              type="text"
              v-model="editableAtendimento.descricao"
              required
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200"
            >
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Valor (R$)</label>
              <input
                type="number"
                step="0.01"
                v-model="editableAtendimento.valor"
                required
                class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200"
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Data</label>
              <input
                type="date"
                v-model="editableAtendimento.data"
                required
                class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200"
              >
            </div>
          </div>

          <div class="flex justify-end space-x-4 pt-4">
            <button
              type="button"
              @click="closeEditModal"
              class="px-4 py-2 bg-gray-100 text-gray-600 rounded-xl hover:bg-gray-200 transition-all duration-200"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-indigo-700 transform hover:scale-[1.02] transition-all duration-200 shadow-md hover:shadow-lg"
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
import { computed, onMounted, ref } from 'vue';
import api from '@/services/api';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';

const { successCreate, successUpdate, successDelete } = useSuccessMessage();
const { showError, showApiError } = useErrorMessage();
const { confirmDelete } = useConfirmation();

const atendimentos = ref([]);
const pets = ref([]);
const clientes = ref([]);

const loading = ref(true);
const error = ref(null);

const showCreateModal = ref(false);
const showEditModal = ref(false);

const newAtendimento = ref({
  pet_id: '',
  descricao: '',
  valor: '',
  data: ''
});

const editableAtendimento = ref({
  id: null,
  pet_id: '',
  descricao: '',
  valor: '',
  data: '',
  cliente_nome: ''
});

const petOptions = computed(() =>
  pets.value.map((pet) => {
    const cliente = clientes.value.find((item) => item.id === pet.cliente_id);
    return {
      id: pet.id,
      nome: pet.nome,
      clienteNome: cliente ? cliente.nome : 'Desconhecido'
    };
  })
);

const fetchData = async () => {
  loading.value = true;
  error.value = null;
  try {
    const [atendimentosRes, petsRes, clientesRes] = await Promise.all([
      api.get('/atendimentos'),
      api.get('/pets'),
      api.get('/clientes')
    ]);

    atendimentos.value = atendimentosRes.data;
    pets.value = petsRes.data;
    clientes.value = clientesRes.data;
  } catch (err) {
    console.error('Falha ao buscar atendimentos:', err);
    error.value = err;
  } finally {
    loading.value = false;
  }
};

const openCreateModal = () => {
  newAtendimento.value = { pet_id: '', descricao: '', valor: '', data: '' };
  showCreateModal.value = true;
};

const closeCreateModal = () => {
  showCreateModal.value = false;
};

const handleCreate = async () => {
  if (!newAtendimento.value.pet_id) {
    showError('Selecione um pet para vincular o atendimento.', { title: 'Pet Obrigatório' });
    return;
  }

  try {
    await api.post(`/pets/${newAtendimento.value.pet_id}/atendimentos`, {
      descricao: newAtendimento.value.descricao,
      valor: parseFloat(newAtendimento.value.valor),
      data: newAtendimento.value.data
    });
    closeCreateModal();
    await fetchData();
    successCreate('Atendimento');
  } catch (err) {
    console.error('Erro ao criar atendimento:', err);
    showApiError(err, 'Não foi possível criar o atendimento.');
  }
};

const openEditModal = (atendimento) => {
  editableAtendimento.value = {
    id: atendimento.id,
    pet_id: atendimento.pet_id,
    descricao: atendimento.descricao,
    valor: atendimento.valor,
    data: atendimento.data,
    cliente_nome: atendimento.cliente_nome
  };
  showEditModal.value = true;
};

const closeEditModal = () => {
  showEditModal.value = false;
};

const handleUpdate = async () => {
  try {
    await api.put(`/atendimentos/${editableAtendimento.value.id}`, {
      descricao: editableAtendimento.value.descricao,
      valor: parseFloat(editableAtendimento.value.valor),
      data: editableAtendimento.value.data
    });
    closeEditModal();
    await fetchData();
    successUpdate('Atendimento');
  } catch (err) {
    console.error('Erro ao atualizar atendimento:', err);
    showApiError(err, 'Não foi possível atualizar o atendimento.');
  }
};

const handleDelete = async (atendimentoId) => {
  const confirmed = await confirmDelete('este atendimento');
  
  if (!confirmed) return;
  
  try {
    await api.delete(`/atendimentos/${atendimentoId}`);
    await fetchData();
    successDelete('Atendimento');
  } catch (err) {
    console.error('Erro ao excluir atendimento:', err);
    showApiError(err, 'Não foi possível excluir o atendimento.');
  }
};

const getPetNome = (petId) => {
  const pet = pets.value.find(p => p.id === petId);
  return pet ? pet.nome : 'Pet não encontrado';
};

const formatarData = (dataStr) => {
  if (!dataStr) {
    return '—';
  }
  

  const [ano, mes, dia] = dataStr.split('-').map(Number);
  const data = new Date(ano, mes - 1, dia); // mes - 1 porque Date usa índice 0 para janeiro
  
  if (Number.isNaN(data.getTime())) {
    return dataStr;
  }
  
  return new Intl.DateTimeFormat('pt-BR').format(data);
};

onMounted(() => {
  fetchData();
});
</script>
