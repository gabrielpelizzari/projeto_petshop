<template>
  <div class="space-y-8">
    <!-- Header Section -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Gerenciamento de Clientes</h1>
        <p class="mt-2 text-gray-600">Controle completo dos clientes cadastrados</p>
      </div>
      <RouterLink
        to="/dashboard/admin/clientes/novo"
        class="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-indigo-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
      >
        <span class="flex items-center space-x-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
          </svg>
          <span>Novo Cliente</span>
        </span>
      </RouterLink>
    </div>


    <!-- Main Content -->
    <div class="bg-white/60 backdrop-blur-sm rounded-2xl border border-gray-100 shadow-lg overflow-hidden">
      <div class="p-6 border-b border-gray-200/50">
        <h2 class="text-xl font-semibold text-gray-900">Clientes Cadastrados</h2>
        <p class="text-sm text-gray-600 mt-1">{{ clientes.length }} cliente(s) registrado(s)</p>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full">
          <thead class="bg-gradient-to-r from-gray-50 to-gray-100">
            <tr>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">ID</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Nome</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">CPF</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Data de Cadastro</th>
              <th class="py-4 px-6 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Ações</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr
              v-for="(cliente, index) in clientes"
              :key="cliente.id"
              class="hover:bg-gray-50/50 transition-colors duration-200"
            >
              <td class="py-4 px-6 text-sm font-medium text-gray-900">{{ cliente.id }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ cliente.nome }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ formatCpf(cliente.cpf) }}</td>
              <td class="py-4 px-6 text-sm text-gray-900">{{ formatarData(cliente.data_cadastro) }}</td>
              <td class="py-4 px-6 text-sm">
                <div class="flex space-x-2">
                  <RouterLink
                    :to="{ name: 'admin-cliente-view', params: { id: cliente.id } }"
                    class="px-3 py-1.5 text-xs font-medium text-green-700 bg-green-100 rounded-lg hover:bg-green-200 transition-colors duration-200"
                  >
                    Visualizar
                  </RouterLink>
                  <RouterLink
                    :to="`/dashboard/admin/clientes/${cliente.id}/edit`"
                    class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-100 rounded-lg hover:bg-blue-200 transition-colors duration-200"
                  >
                    Editar
                  </RouterLink>
                  <button
                    @click="handleDeleteCliente(cliente.id)"
                    class="px-3 py-1.5 text-xs font-medium text-red-700 bg-red-100 rounded-lg hover:bg-red-200 transition-colors duration-200"
                  >
                    Excluir
                  </button>
                </div>
              </td>
            </tr>
            <tr v-if="clientes.length === 0">
              <td colspan="5" class="py-12 text-center">
                <div class="flex flex-col items-center space-y-3">
                  <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
                  </svg>
                  <p class="text-gray-500 font-medium">Nenhum cliente cadastrado</p>
                  <p class="text-gray-400 text-sm">Clique em "Novo Cliente" para começar</p>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>


    <!-- Modal de Editar Cliente -->
    <div v-if="editingClientId" class="fixed inset-0 bg-black/50 backdrop-blur-sm overflow-y-auto h-full w-full flex items-center justify-center p-4 z-50">
      <div class="bg-white/90 backdrop-blur-md rounded-2xl p-8 w-full max-w-lg shadow-2xl border border-gray-200">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-2xl font-bold text-gray-900">Editar Cliente</h3>
          <button
            @click="editingClientId = null"
            class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
        <form @submit.prevent="handleUpdateCliente" class="space-y-6">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Nome Completo</label>
            <input 
              type="text" 
              v-model="editableClientData.nome" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200"
            >
          </div>
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Nova Senha (opcional)</label>
            <input 
              type="password" 
              v-model="editableClientData.nova_senha" 
              placeholder="Deixe em branco para não alterar"
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400"
            >
          </div>
          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button" 
              @click="editingClientId = null" 
              class="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
            >
              Cancelar
            </button>
            <button 
              type="submit" 
              class="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-indigo-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
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
import { useCpfFormatter } from '@/composables/useCpfFormatter';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';

const { successUpdate, successDelete } = useSuccessMessage();
const { showApiError } = useErrorMessage();
const { confirmDelete } = useConfirmation();
const clientes = ref([]);
const loading = ref(true);
const error = ref(null);
const { formatCpf } = useCpfFormatter();

const editingClientId = ref(null);
const editableClientData = ref({ nome: '', nova_senha: '' });

const formatarData = (data) => {
  if (!data) return '';
  const [ano, mes, dia] = data.split('-');
  return `${dia}/${mes}/${ano}`;
};

const fetchData = async () => {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.get('/clientes');
    clientes.value = response.data;
  } catch (err) {
    console.error('Erro ao buscar clientes:', err);
    showApiError(err);
    error.value = err;
  } finally {
    loading.value = false;
  }
};

const openEditForm = (cliente) => {
  editingClientId.value = cliente.id;
  editableClientData.value.nome = cliente.nome;
  editableClientData.value.nova_senha = '';
};

const handleUpdateCliente = async () => {
  if (!editingClientId.value) return;
  try {
    await api.put(`/clientes/${editingClientId.value}`, editableClientData.value);
    successUpdate('Cliente');
    editingClientId.value = null;
    fetchData();
  } catch (err) {
    console.error('Erro ao atualizar cliente:', err);
    showApiError(err.response?.data?.detail || 'Não foi possível atualizar o cliente.');
  }
};


const handleDeleteCliente = async (clienteId) => {
  const confirmed = await confirmDelete('este cliente');
  
  if (!confirmed) return;
  
  try {
    await api.delete(`/clientes/${clienteId}`);
    successDelete('Cliente');
    fetchData();
  } catch (err) {
    console.error('Erro ao excluir cliente:', err);
    showApiError(err.response?.data?.detail || 'Não foi possível excluir o cliente.');
  }
};

onMounted(() => {
  fetchData();
});
</script>
