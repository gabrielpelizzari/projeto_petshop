<template>
  <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg hover:shadow-xl transition-all duration-300 group">
    <!-- Pet Header -->
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-3">
        <div class="w-12 h-12 bg-gradient-to-br from-green-500 to-emerald-500 rounded-full flex items-center justify-center shadow-lg">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
          </svg>
        </div>
        <div>
          <h3 class="text-xl font-bold text-gray-900">{{ pet.nome }}</h3>
          <p class="text-sm text-gray-600">{{ getRacaNome(pet.raca_id) }}</p>
        </div>
      </div>
      
      <!-- Actions -->
      <div class="flex space-x-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
        <button
          v-if="!isEditing"
          @click="startEdit"
          class="p-2 text-green-600 hover:text-green-700 hover:bg-green-50 rounded-lg transition-colors duration-200"
          title="Editar pet"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
          </svg>
        </button>

        <button
          v-if="!isEditing && pet.atendimentos.length === 0"
          @click="$emit('delete-pet', pet.id)"
          class="p-2 text-red-600 hover:text-red-700 hover:bg-red-50 rounded-lg transition-colors duration-200"
          title="Excluir pet"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Pet Info - View Mode -->
    <div v-if="!isEditing" class="space-y-3">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-3">
          <div class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3a2 2 0 012-2h4a2 2 0 012 2v4m-6 4v10m6-10v10m-6-4h6"/>
            </svg>
            <div>
              <p class="text-xs text-green-600 font-medium uppercase tracking-wide">Raça</p>
              <p class="text-sm font-semibold text-gray-900">{{ getRacaNome(pet.raca_id) }}</p>
            </div>
          </div>
        </div>
        
        <div class="bg-gradient-to-r from-blue-50 to-cyan-50 rounded-xl p-3">
          <div class="flex items-center space-x-2">
            <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3a2 2 0 012-2h4a2 2 0 012 2v4m-6 4v10m6-10v10m-6-4h6"/>
            </svg>
            <div>
              <p class="text-xs text-blue-600 font-medium uppercase tracking-wide">Nascimento</p>
              <p class="text-sm font-semibold text-gray-900">{{ formatarData(pet.data_nascimento) }}</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Age Badge -->
      <div class="flex justify-center">
        <div class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-gradient-to-r from-purple-100 to-pink-100 text-purple-700">
          <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          {{ calcularIdade(pet.data_nascimento) }}
        </div>
      </div>

      <!-- Atendimentos Section -->
      <div v-if="pet.atendimentos && pet.atendimentos.length > 0" class="mt-4 pt-3 border-t border-gray-200/80">
        <h4 class="text-xs font-semibold text-gray-700 mb-2 flex items-center justify-between">
          <span class="flex items-center">
            <svg class="w-3 h-3 mr-1 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3a1 1 0 011-1h6a1 1 0 011 1v4m-5 8v4m-2-4h4m-4 4H9m6 0h-2m-4-8a2 2 0 01-2-2v-2a2 2 0 012-2h8a2 2 0 012 2v2a2 2 0 01-2 2h-2l-4 4z"></path>
            </svg>
            Atendimentos
          </span>
          <span class="text-xs text-gray-500 font-normal">{{ pet.atendimentos.length }}</span>
        </h4>
        <div class="space-y-1">
          <AtendimentoCard 
            v-for="atendimento in atendimentosLimitados" 
            :key="atendimento.id" 
            :atendimento="atendimento"
          />
          
          <!-- Botão Ver todos / Ver menos -->
          <div v-if="pet.atendimentos.length > 3" class="text-center pt-2">
            <button 
              @click="showAllAtendimentos = !showAllAtendimentos"
              class="text-xs text-blue-600 hover:text-blue-700 font-medium flex items-center justify-center space-x-1 mx-auto px-2 py-1 rounded-md hover:bg-blue-50 transition-colors duration-200"
            >
              <span v-if="!showAllAtendimentos">
                Ver todos ({{ pet.atendimentos.length }})
              </span>
              <span v-else>
                Ver menos
              </span>
              <svg 
                class="w-3 h-3 transition-transform duration-200" 
                :class="{ 'rotate-180': showAllAtendimentos }"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Pet Info - Edit Mode -->
    <div v-else class="space-y-4">
      <form @submit.prevent="saveEdit" class="space-y-4">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-2">Nome do Pet</label>
          <input 
            type="text" 
            v-model="editData.nome" 
            required 
            class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
          >
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Data de Nascimento</label>
            <input 
              type="date" 
              v-model="editData.data_nascimento" 
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
                {{ getDateValidationMessage() }}
              </span>
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Raça</label>
            <select 
              v-model="editData.raca_id" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
            >
              <option disabled value="">Selecione a raça</option>
              <option v-for="raca in racas" :key="raca.id" :value="raca.id">{{ raca.nome }}</option>
            </select>
          </div>
        </div>
        
        <div class="flex justify-end space-x-3 pt-4">
          <button 
            type="button" 
            @click="cancelEdit" 
            class="px-4 py-2 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            :disabled="!isEditFormValid"
            :class="[
              'px-6 py-2 font-semibold rounded-xl transform transition-all duration-200 shadow-lg',
              !isEditFormValid 
                ? 'bg-gray-400 cursor-not-allowed opacity-50' 
                : 'bg-gradient-to-r from-green-600 to-emerald-600 text-white hover:from-green-700 hover:to-emerald-700 hover:scale-105'
            ]"
          >
            Salvar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import AtendimentoCard from './AtendimentoCard.vue';
import { useErrorMessage } from '@/composables/useErrorMessage';

const { showError } = useErrorMessage();

const props = defineProps({
  pet: {
    type: Object,
    required: true
  },
  racas: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['update-pet', 'delete-pet']);

const isEditing = ref(false);
const editData = ref({});
const showAllAtendimentos = ref(false);

// Limita os atendimentos exibidos para manter o card compacto.
const atendimentosLimitados = computed(() => {
  if (!props.pet.atendimentos) return [];
  if (showAllAtendimentos.value) return props.pet.atendimentos;
  return props.pet.atendimentos.slice(0, 3);
});

// Data máxima permitida (hoje).
const maxDate = computed(() => {
  const today = new Date();
  return today.toISOString().split('T')[0];
});

// Verifica se a data de nascimento de edição é válida (não é no futuro).
const isEditDateValid = computed(() => {
  // Se não há data selecionada, considera inválido (data é obrigatória para pets)
  if (!editData.value.data_nascimento || editData.value.data_nascimento.trim() === '') {
    return false;
  }
  const selectedDate = new Date(editData.value.data_nascimento);
  const today = new Date();
  today.setHours(23, 59, 59, 999); // Permite até o final do dia atual
  return selectedDate <= today;
});

const showEditDateValidation = computed(() => {
  return isEditing.value;
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
  return editData.value.nome && editData.value.nome.trim() && 
         editData.value.raca_id && 
         isEditDateValid.value;
});

const getDateValidationMessage = () => {
  if (!editData.value.data_nascimento || editData.value.data_nascimento.trim() === '') {
    return 'A data de nascimento é obrigatória';
  }
  
  const selectedDate = new Date(editData.value.data_nascimento);
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  
  if (selectedDate > today) {
    return 'A data de nascimento não pode ser uma data futura';
  }
  
  return 'Data válida';
};


const getRacaNome = (racaId) => {
  const raca = props.racas.find(r => r.id === racaId);
  return raca ? raca.nome : 'Não informado';
};


const formatarData = (dataStr) => {
  if (!dataStr) return 'Não informado';
  const [ano, mes, dia] = dataStr.split('-').map(Number);
  const data = new Date(ano, mes - 1, dia); // mes - 1 porque Date usa índice 0 para janeiro
  
  return data.toLocaleDateString('pt-BR');
};


const calcularIdade = (dataNascimento) => {
  if (!dataNascimento) return 'Idade não informada';
  const hoje = new Date();
  const [ano, mes, dia] = dataNascimento.split('-').map(Number);
  const nascimento = new Date(ano, mes - 1, dia);
  
  const diffTime = Math.abs(hoje - nascimento);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  if (diffDays < 30) {
    return `${diffDays} dias`;
  } else if (diffDays < 365) {
    const meses = Math.floor(diffDays / 30);
    return `${meses} ${meses === 1 ? 'mês' : 'meses'}`;
  } else {
    const anos = Math.floor(diffDays / 365);
    const mesesRestantes = Math.floor((diffDays % 365) / 30);
    if (mesesRestantes === 0) {
      return `${anos} ${anos === 1 ? 'ano' : 'anos'}`;
    }
    return `${anos} ${anos === 1 ? 'ano' : 'anos'} e ${mesesRestantes} ${mesesRestantes === 1 ? 'mês' : 'meses'}`;
  }
};

const startEdit = () => {
  editData.value = { ...props.pet };
  isEditing.value = true;
};

const cancelEdit = () => {
  isEditing.value = false;
  editData.value = {};
  showAllAtendimentos.value = false; // Recolhe atendimentos se estavam expandidos
};


const saveEdit = () => {
  if (!editData.value.nome || !editData.value.nome.trim()) {
    showError('O nome do pet é obrigatório.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!editData.value.raca_id) {
    showError('A raça do pet é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!editData.value.data_nascimento || editData.value.data_nascimento.trim() === '') {
    showError('A data de nascimento é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!isEditDateValid.value) {
    showError('A data de nascimento não pode ser no futuro.', { title: 'Data Inválida' });
    return;
  }
  
  emit('update-pet', editData.value);
  isEditing.value = false;
};
</script>
