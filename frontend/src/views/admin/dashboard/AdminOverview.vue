<template>
  <div class="space-y-8">
    <!-- Header Section -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Dashboard Administrativo</h1>
        <p class="mt-2 text-gray-600">Visão geral do sistema PetHub</p>
      </div>
      <div class="text-right">
        <p class="text-sm text-gray-500">Último acesso</p>
        <p class="text-lg font-semibold text-gray-900">{{ currentDate }}</p>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div v-for="i in 4" :key="i" class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg animate-pulse">
        <div class="flex items-center justify-between">
          <div class="flex-1">
            <div class="h-4 bg-gray-200 rounded w-3/4 mb-3"></div>
            <div class="h-8 bg-gray-200 rounded w-1/2 mb-2"></div>
            <div class="h-3 bg-gray-200 rounded w-2/3"></div>
          </div>
          <div class="w-12 h-12 bg-gray-200 rounded-xl"></div>
        </div>
      </div>
    </div>

    <!-- Stats Cards -->
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <!-- Total Clientes -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg hover:shadow-xl transition-all duration-300">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total de Clientes</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.totalClientes }}</p>
            <p class="text-sm text-green-600 mt-1">
              <span class="inline-flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>
                </svg>
                +12% este mês
              </span>
            </p>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Total Pets -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg hover:shadow-xl transition-all duration-300">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Total de Pets</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.totalPets }}</p>
            <p class="text-sm text-green-600 mt-1">
              <span class="inline-flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>
                </svg>
                +8% este mês
              </span>
            </p>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Atendimentos Hoje -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg hover:shadow-xl transition-all duration-300">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Atendimentos Hoje</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.atendimentosHoje }}</p>
            <p class="text-sm text-blue-600 mt-1">
              <span class="inline-flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                {{ stats.proximoAtendimento }}
              </span>
            </p>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Receita Mensal -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg hover:shadow-xl transition-all duration-300">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">Receita Mensal</p>
            <p class="text-3xl font-bold text-gray-900 mt-2">R$ {{ stats.receitaMensal.toLocaleString() }}</p>
            <p class="text-sm text-green-600 mt-1">
              <span class="inline-flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/>
                </svg>
                +15% este mês
              </span>
            </p>
          </div>
          <div class="w-12 h-12 bg-yellow-100 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"/>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Ações Rápidas -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Ações Rápidas</h3>
        <div class="space-y-3">
          <RouterLink
            to="/dashboard/admin/atendimentos"
            class="flex items-center p-4 bg-gradient-to-r from-purple-50 to-purple-100 rounded-xl hover:from-purple-100 hover:to-purple-200 transition-all duration-200 group"
          >
            <div class="w-10 h-10 bg-purple-500 rounded-lg flex items-center justify-center mr-4">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900 group-hover:text-purple-700">Novo Atendimento</p>
              <p class="text-sm text-gray-600">Registrar atendimento realizado</p>
            </div>
          </RouterLink>
          <RouterLink
            to="/dashboard/admin/clientes"
            class="flex items-center p-4 bg-gradient-to-r from-blue-50 to-blue-100 rounded-xl hover:from-blue-100 hover:to-blue-200 transition-all duration-200 group"
          >
            <div class="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center mr-4">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"/>
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900 group-hover:text-blue-700">Adicionar Cliente</p>
              <p class="text-sm text-gray-600">Cadastrar novo cliente no sistema</p>
            </div>
          </RouterLink>

          <RouterLink
            to="/dashboard/admin/pets"
            class="flex items-center p-4 bg-gradient-to-r from-green-50 to-green-100 rounded-xl hover:from-green-100 hover:to-green-200 transition-all duration-200 group"
          >
            <div class="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center mr-4">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900 group-hover:text-green-700">Registrar Pet</p>
              <p class="text-sm text-gray-600">Adicionar novo pet ao sistema</p>
            </div>
          </RouterLink>
          <RouterLink
            to="/dashboard/admin/racas"
            class="flex items-center p-4 bg-gradient-to-r from-yellow-50 to-yellow-100 rounded-xl hover:from-yellow-100 hover:to-yellow-200 transition-all duration-200 group"
          >
            <div class="w-10 h-10 bg-yellow-500 rounded-lg flex items-center justify-center mr-4">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
              </svg>
            </div>
            <div>
              <p class="font-medium text-gray-900 group-hover:text-green-700">Registrar Raça</p>
              <p class="text-sm text-gray-600">Adicionar nova raça ao sistema</p>
            </div>
          </RouterLink>

     
        </div>
      </div>

      <!-- Atividades Recentes -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg">
        <h3 class="text-lg font-semibold text-gray-900 mb-4">Atividades Recentes</h3>
        
        <!-- Loading State para Atividades -->
        <div v-if="loading" class="space-y-4">
          <div v-for="i in 4" :key="i" class="flex items-start space-x-3 animate-pulse">
            <div class="w-8 h-8 bg-gray-200 rounded-full"></div>
            <div class="flex-1 min-w-0">
              <div class="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
              <div class="h-3 bg-gray-200 rounded w-full mb-1"></div>
              <div class="h-3 bg-gray-200 rounded w-1/4"></div>
            </div>
          </div>
        </div>

        <!-- Atividades Carregadas -->
        <div v-else-if="atividadesRecentes.length > 0" class="space-y-4">
          <div v-for="atividade in atividadesRecentes" :key="atividade.id" class="flex items-start space-x-3">
            <div class="w-8 h-8 rounded-full flex items-center justify-center" :class="atividade.bgColor">
              <svg class="w-4 h-4" :class="atividade.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="atividade.iconPath"/>
              </svg>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-900">{{ atividade.titulo }}</p>
              <p class="text-sm text-gray-600">{{ atividade.descricao }}</p>
              <p class="text-xs text-gray-400 mt-1">{{ atividade.tempo }}</p>
            </div>
          </div>
        </div>

        <!-- Estado Vazio -->
        <div v-else class="text-center py-8">
          <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <h3 class="mt-2 text-sm font-medium text-gray-900">Nenhuma atividade recente</h3>
          <p class="mt-1 text-sm text-gray-500">As atividades aparecerão aqui conforme você usar o sistema.</p>
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


const stats = ref({
  totalClientes: 0,
  totalPets: 0,
  totalRacas: 0,
  atendimentosHoje: 0,
  proximoAtendimento: 'Nenhum agendado',
  receitaMensal: 0
});

const atividadesRecentes = ref([]);
const loading = ref(true);
const { showApiError } = useErrorMessage();


const currentDate = computed(() => {
  return new Date().toLocaleDateString('pt-BR', {
    day: '2-digit',
    month: 'long',
    year: 'numeric'
  });
});


// Carrega dados estatísticos do dashboard.

const loadDashboardData = async () => {
  loading.value = true;
  try {

    const [clientesRes, petsRes, racasRes, atendimentosRes] = await Promise.all([
      api.get('/clientes'),
      api.get('/pets'),
      api.get('/racas'),
      api.get('/atendimentos')
    ]);

    // Atualiza estatísticas
    stats.value.totalClientes = clientesRes.data.length;
    stats.value.totalPets = petsRes.data.length;
    stats.value.totalRacas = racasRes.data.length;
    
    // Calcula atendimentos de hoje
    const hoje = new Date().toISOString().split('T')[0];
    const atendimentosHoje = atendimentosRes.data.filter(atendimento => {
      return atendimento.data === hoje;
    });
    stats.value.atendimentosHoje = atendimentosHoje.length;
    
    // Calcula receita mensal (soma dos valores dos atendimentos do mês atual)
    const mesAtual = new Date().getMonth();
    const anoAtual = new Date().getFullYear();
    const receitaMensal = atendimentosRes.data
      .filter(atendimento => {
        const [ano, mes] = atendimento.data.split('-').map(Number);
        return ano === anoAtual && mes - 1 === mesAtual;
      })
      .reduce((total, atendimento) => total + atendimento.valor, 0);
    stats.value.receitaMensal = receitaMensal;

    // Gera atividades recentes baseadas nos dados reais
    generateAtividadesRecentes(clientesRes.data, petsRes.data, atendimentosRes.data);

  } catch (error) {
    console.error('Erro ao carregar dados do dashboard:', error);
    showApiError(error);
  } finally {
    loading.value = false;
  }
};

// Gera atividades recentes baseadas nos dados
const generateAtividadesRecentes = (clientes, pets, atendimentos) => {
  const atividades = [];

  // Adiciona clientes recentes (últimos 3)
  const clientesRecentes = clientes
    .sort((a, b) => new Date(b.data_cadastro) - new Date(a.data_cadastro))
    .slice(0, 2);

  clientesRecentes.forEach((cliente, index) => {
    atividades.push({
      id: `cliente-${cliente.id}`,
      titulo: 'Novo cliente cadastrado',
      descricao: `${cliente.nome} foi adicionado ao sistema`,
      tempo: getTempoRelativo(cliente.data_cadastro),
      bgColor: 'bg-blue-100',
      iconColor: 'text-blue-600',
      iconPath: 'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z'
    });
  });

  // Adiciona pets recentes (últimos 2)
  const petsRecentes = pets.slice(-2);
  petsRecentes.forEach((pet, index) => {
    atividades.push({
      id: `pet-${pet.id}`,
      titulo: 'Pet cadastrado',
      descricao: `${pet.nome} foi adicionado como novo paciente`,
      tempo: 'recentemente',
      bgColor: 'bg-purple-100',
      iconColor: 'text-purple-600',
      iconPath: 'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z'
    });
  });

  // Adiciona atendimentos recentes (últimos 2)
  const atendimentosRecentes = atendimentos
    .sort((a, b) => new Date(b.data) - new Date(a.data))
    .slice(0, 2);

  atendimentosRecentes.forEach((atendimento, index) => {
    const pet = pets.find(p => p.id === atendimento.pet_id);
    atividades.push({
      id: `atendimento-${atendimento.id}`,
      titulo: 'Atendimento realizado',
      descricao: `${atendimento.descricao} - ${pet ? pet.nome : 'Pet'}`,
      tempo: getTempoRelativo(atendimento.data),
      bgColor: 'bg-green-100',
      iconColor: 'text-green-600',
      iconPath: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z'
    });
  });

  // Limita a 6 atividades e ordena por mais recentes
  atividadesRecentes.value = atividades.slice(0, 6);
};


// Calcula tempo relativo para exibição.

const getTempoRelativo = (dataString) => {
  const [ano, mes, dia] = dataString.split('-').map(Number);
  const data = new Date(ano, mes - 1, dia);
  const agora = new Date();
  const diffTime = Math.abs(agora - data);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

  if (diffDays === 0) return 'hoje';
  if (diffDays === 1) return 'ontem';
  if (diffDays < 7) return `há ${diffDays} dias`;
  if (diffDays < 30) return `há ${Math.floor(diffDays / 7)} semanas`;
  return `há ${Math.floor(diffDays / 30)} meses`;
};

onMounted(() => {
  loadDashboardData();
});
</script>
