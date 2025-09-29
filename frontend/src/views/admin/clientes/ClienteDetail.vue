<template>
  <div class="space-y-8">
    <!-- Header -->
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-4">
        <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl flex items-center justify-center shadow-lg">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
          </svg>
        </div>
        <div>
          <h1 class="text-3xl font-bold text-gray-900">{{ cliente.nome }}</h1>
          <p class="text-gray-600">Perfil Completo do Cliente</p>
        </div>
      </div>
      <div class="flex items-center space-x-3">
        <RouterLink
          :to="{ name: 'admin-cliente-edit', params: { id: clienteId } }"
          class="px-4 py-2 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition-colors duration-200 flex items-center space-x-2"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
          <span>Editar Cliente</span>
        </RouterLink>
        <RouterLink
          to="/dashboard/admin/clientes"
          class="px-4 py-2 bg-gray-600 text-white font-semibold rounded-xl hover:bg-gray-700 transition-colors duration-200 flex items-center space-x-2"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          <span>Voltar</span>
        </RouterLink>
      </div>
    </div>

      <!-- Loading State -->
      <div v-if="loading" class="p-6">
        <div class="animate-pulse space-y-6">
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div v-for="i in 3" :key="i" class="bg-gray-200 rounded-2xl h-48"></div>
          </div>
        </div>
      </div>

    <!-- Content -->
    <div v-else class="space-y-8">
        <!-- Informações Pessoais -->
        <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-4 border border-blue-100">
          <div class="flex items-center space-x-2 mb-3">
            <div class="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center">
              <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900">Informações Pessoais</h3>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <div class="bg-white/60 rounded-lg p-3">
              <p class="text-xs font-medium text-gray-600">Nome Completo</p>
              <p class="text-sm font-semibold text-gray-900 mt-1">{{ cliente.nome }}</p>
            </div>
            <div class="bg-white/60 rounded-lg p-3">
              <p class="text-xs font-medium text-gray-600">CPF</p>
              <p class="text-sm font-semibold text-gray-900 mt-1">{{ formatCpf(cliente.cpf) }}</p>
            </div>
            <div class="bg-white/60 rounded-lg p-3">
              <p class="text-xs font-medium text-gray-600">Data de Cadastro</p>
              <p class="text-sm font-semibold text-gray-900 mt-1">{{ formatarData(cliente.data_cadastro) }}</p>
            </div>
          </div>
        </div>

        <!-- Contato e Endereço -->
        <div class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-4 border border-green-100">
          <div class="flex items-center space-x-2 mb-3">
            <div class="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center">
              <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900">Contato e Endereço</h3>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Contato -->
            <div class="space-y-3">
              <h4 class="text-sm font-semibold text-gray-800">Informações de Contato</h4>
              <div class="space-y-2">
                <div class="bg-white/60 rounded-lg p-3">
                  <p class="text-xs font-medium text-gray-600">Email</p>
                  <p class="text-sm font-semibold text-gray-900 mt-1">{{ contatoEmail }}</p>
                </div>
                <div class="bg-white/60 rounded-lg p-3">
                  <p class="text-xs font-medium text-gray-600">Telefone</p>
                  <p class="text-sm font-semibold text-gray-900 mt-1">{{ contatoTelefoneFormatado }}</p>
                </div>
              </div>
            </div>

            <!-- Endereço -->
            <div class="space-y-3">
              <h4 class="text-sm font-semibold text-gray-800">Endereço Principal</h4>
              <div v-if="enderecoPrincipal" class="bg-white/60 rounded-lg p-3">
                <p class="text-sm font-semibold text-gray-900">{{ enderecoPrincipal.logradouro }}</p>
                <p class="text-xs text-gray-600 mt-1">{{ enderecoPrincipal.bairro }}, {{ enderecoPrincipal.cidade }}</p>
                <p v-if="enderecoPrincipal.complemento" class="text-xs text-gray-600">{{ enderecoPrincipal.complemento }}</p>
                <span v-if="enderecoPrincipal.tag" class="inline-block mt-2 px-2 py-1 bg-green-100 text-green-800 text-xs font-medium rounded-full">
                  {{ enderecoPrincipal.tag }}
                </span>
              </div>
              <div v-else class="bg-white/60 rounded-lg p-3">
                <p class="text-sm text-gray-500">Endereço não informado</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Estatísticas Rápidas -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="bg-gradient-to-r from-purple-50 to-purple-100 rounded-xl p-4 border border-purple-200">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs font-medium text-purple-600">Total de Pets</p>
                <p class="text-2xl font-bold text-purple-900 mt-1">{{ pets.length }}</p>
              </div>
              <div class="w-10 h-10 bg-purple-500 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
            </div>
          </div>

          <div class="bg-gradient-to-r from-orange-50 to-orange-100 rounded-xl p-4 border border-orange-200">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs font-medium text-orange-600">Total de Atendimentos</p>
                <p class="text-2xl font-bold text-orange-900 mt-1">{{ atendimentos.length }}</p>
              </div>
              <div class="w-10 h-10 bg-orange-500 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                </svg>
              </div>
            </div>
          </div>

          <div class="bg-gradient-to-r from-teal-50 to-teal-100 rounded-xl p-4 border border-teal-200">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-xs font-medium text-teal-600">Valor Total Gasto</p>
                <p class="text-2xl font-bold text-teal-900 mt-1">R$ {{ totalGasto.toLocaleString() }}</p>
              </div>
              <div class="w-10 h-10 bg-teal-500 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
                </svg>
              </div>
            </div>
          </div>
        </div>

        <!-- Pets do Cliente -->
        <div class="bg-gradient-to-r from-pink-50 to-rose-50 rounded-xl p-4 border border-pink-100">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-8 h-8 bg-pink-500 rounded-lg flex items-center justify-center">
              <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900">Pets Cadastrados</h3>
          </div>

          <div v-if="pets.length === 0" class="text-center py-8">
            <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <h3 class="mt-2 text-sm font-medium text-gray-900">Nenhum pet cadastrado</h3>
            <p class="mt-1 text-sm text-gray-500">Este cliente ainda não possui pets cadastrados.</p>
          </div>

          <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
            <div v-for="pet in pets" :key="pet.id" class="bg-white/70 rounded-lg p-3 border border-pink-200 hover:shadow-md transition-all duration-200">
              <div class="flex items-center space-x-2 mb-2">
                <div class="w-8 h-8 bg-pink-500 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                  </svg>
                </div>
                <div>
                  <h4 class="text-sm font-semibold text-gray-900">{{ pet.nome }}</h4>
                  <p class="text-xs text-gray-600">{{ getRacaNome(pet.raca_id) }}</p>
                </div>
              </div>
              <div class="space-y-1 text-xs">
                <p class="text-gray-600">
                  <span class="font-medium">Nascimento:</span> {{ formatarData(pet.data_nascimento) }}
                </p>
                <p class="text-gray-600">
                  <span class="font-medium">Idade:</span> {{ calcularIdade(pet.data_nascimento) }}
                </p>
                <p class="text-gray-600">
                  <span class="font-medium">Atendimentos:</span> {{ getAtendimentosPorPet(pet.id).length }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Histórico de Atendimentos -->
        <div class="bg-gradient-to-r from-indigo-50 to-blue-50 rounded-xl p-4 border border-indigo-100">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-8 h-8 bg-indigo-500 rounded-lg flex items-center justify-center">
              <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900">Histórico de Atendimentos</h3>
          </div>

          <div v-if="atendimentos.length === 0" class="text-center py-8">
            <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
            </svg>
            <h3 class="mt-2 text-sm font-medium text-gray-900">Nenhum atendimento realizado</h3>
            <p class="mt-1 text-sm text-gray-500">Este cliente ainda não possui atendimentos registrados.</p>
          </div>

          <div v-else class="space-y-3">
            <div v-for="atendimento in atendimentosOrdenados" :key="atendimento.id" 
                 class="bg-white/70 rounded-lg p-3 border border-indigo-200 hover:shadow-md transition-all duration-200">
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <div class="flex items-center space-x-2 mb-2">
                    <div class="w-6 h-6 bg-indigo-500 rounded-md flex items-center justify-center">
                      <svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                      </svg>
                    </div>
                    <div>
                      <h4 class="text-sm font-semibold text-gray-900">{{ atendimento.descricao }}</h4>
                      <p class="text-xs text-gray-600">{{ getPetNome(atendimento.pet_id) }}</p>
                    </div>
                  </div>
                  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mt-2">
                    <div>
                      <p class="text-xs font-medium text-gray-500">Data</p>
                      <p class="text-xs font-semibold text-gray-900">{{ formatarData(atendimento.data) }}</p>
                    </div>
                    <div>
                      <p class="text-xs font-medium text-gray-500">Valor</p>
                      <p class="text-xs font-semibold text-gray-900">R$ {{ atendimento.valor.toLocaleString() }}</p>
                    </div>
                    <div>
                      <p class="text-xs font-medium text-gray-500">Status</p>
                      <span class="inline-block px-2 py-1 bg-green-100 text-green-800 text-xs font-medium rounded-full">
                        Concluído
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import api from '@/services/api';
import { useErrorMessage } from '@/composables/useErrorMessage';

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

const clienteId = computed(() => parseInt(props.id));

const cliente = ref({});
const pets = ref([]);
const atendimentos = ref([]);
const racas = ref([]);
const loading = ref(true);

const { showApiError } = useErrorMessage();

const totalGasto = computed(() => {
  return atendimentos.value.reduce((total, atendimento) => total + atendimento.valor, 0);
});

const atendimentosOrdenados = computed(() => {
  return [...atendimentos.value].sort((a, b) => new Date(b.data) - new Date(a.data));
});

const enderecoPrincipal = computed(() => {
  const listaEnderecos = cliente.value.enderecos;
  if (Array.isArray(listaEnderecos) && listaEnderecos.length > 0) {
    return listaEnderecos[0];
  }

  if (cliente.value.endereco) {
    return cliente.value.endereco;
  }

  if (cliente.value.logradouro || cliente.value.cidade || cliente.value.bairro) {
    return {
      logradouro: cliente.value.logradouro,
      cidade: cliente.value.cidade,
      bairro: cliente.value.bairro,
      complemento: cliente.value.complemento,
      tag: cliente.value.tag
    };
  }

  return null;
});

const contatoEmail = computed(() => {
  const listaContatos = cliente.value.contatos;
  if (Array.isArray(listaContatos)) {
    const contato = listaContatos.find((item) => item.tipo?.toLowerCase() === 'email');
    if (contato?.valor) {
      return contato.valor;
    }
  }

  return cliente.value.email || 'Não informado';
});

const contatoTelefone = computed(() => {
  const listaContatos = cliente.value.contatos;
  if (Array.isArray(listaContatos)) {
    const contato = listaContatos.find((item) => item.tipo?.toLowerCase() === 'telefone');
    if (contato?.valor) {
      return contato.valor;
    }
  }

  return cliente.value.telefone || 'Não informado';
});

const contatoTelefoneFormatado = computed(() => {
  const telefone = contatoTelefone.value;
  if (!telefone || telefone === 'Não informado') {
    return telefone || 'Não informado';
  }

  const somenteDigitos = telefone.replace(/\D/g, '');

  if (somenteDigitos.length === 11) {
    return `(${somenteDigitos.slice(0, 2)}) ${somenteDigitos.slice(2, 7)}-${somenteDigitos.slice(7)}`;
  }

  if (somenteDigitos.length === 10) {
    return `(${somenteDigitos.slice(0, 2)}) ${somenteDigitos.slice(2, 6)}-${somenteDigitos.slice(6)}`;
  }

  return telefone;
});

const formatCpf = (cpf) => {
  return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
};

const formatarData = (dataString) => {
  const [ano, mes, dia] = dataString.split('-').map(Number);
  const data = new Date(ano, mes - 1, dia);
  return data.toLocaleDateString('pt-BR');
};

const calcularIdade = (dataNascimento) => {
  const [ano, mes, dia] = dataNascimento.split('-').map(Number);
  const nascimento = new Date(ano, mes - 1, dia);
  const hoje = new Date();
  const diffTime = Math.abs(hoje - nascimento);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  if (diffDays < 30) return `${diffDays} dias`;
  if (diffDays < 365) return `${Math.floor(diffDays / 30)} meses`;
  const anos = Math.floor(diffDays / 365);
  const meses = Math.floor((diffDays % 365) / 30);
  return meses > 0 ? `${anos} anos e ${meses} meses` : `${anos} anos`;
};

const getRacaNome = (racaId) => {
  const raca = racas.value.find(r => r.id === racaId);
  return raca ? raca.nome : 'Raça não encontrada';
};

const getPetNome = (petId) => {
  const pet = pets.value.find(p => p.id === petId);
  return pet ? pet.nome : 'Pet não encontrado';
};

const getAtendimentosPorPet = (petId) => {
  return atendimentos.value.filter(a => a.pet_id === petId);
};

const fetchClienteData = async () => {
  loading.value = true;
  try {
    const [clienteRes, petsRes, atendimentosRes, racasRes] = await Promise.all([
      api.get(`/clientes/${clienteId.value}`),
      api.get(`/clientes/${clienteId.value}/pets`),
      api.get('/atendimentos'),
      api.get('/racas')
    ]);

    cliente.value = clienteRes.data;
    pets.value = petsRes.data;
    racas.value = racasRes.data;
    
    // Filtra atendimentos apenas deste cliente
    const petIds = petsRes.data.map(pet => pet.id);
    atendimentos.value = atendimentosRes.data.filter(atendimento => 
      petIds.includes(atendimento.pet_id)
    );

  } catch (error) {
    console.error('Erro ao carregar dados do cliente:', error);
    showApiError(error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchClienteData();
});
</script>
