<template>
  <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg">
    <div class="flex items-center justify-between mb-6">
      <div class="flex items-center space-x-3">
        <div class="w-12 h-12 bg-gradient-to-br from-green-500 to-emerald-500 rounded-full flex items-center justify-center shadow-lg">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
          </svg>
        </div>
        <div>
          <h2 class="text-xl font-semibold text-gray-900">Adicionar Novo Pet</h2>
          <p class="text-sm text-gray-600">Cadastre um novo membro da família</p>
        </div>
      </div>
      <button 
        @click="$emit('close')"
        class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </div>

    <form @submit.prevent="submitForm" class="space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label for="pet-nome" class="block text-sm font-semibold text-gray-700 mb-2">Nome do Pet</label>
          <input 
            type="text" 
            id="pet-nome" 
            v-model="formData.nome" 
            required 
            placeholder="Digite o nome do seu pet"
            class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
          >
        </div>
        
        <div>
          <label for="pet-nascimento" class="block text-sm font-semibold text-gray-700 mb-2">Data de Nascimento *</label>
          <input 
            type="date" 
            id="pet-nascimento" 
            v-model="formData.data_nascimento" 
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
        <label for="pet-raca" class="block text-sm font-semibold text-gray-700 mb-2">Raça</label>
        <select 
          id="pet-raca" 
          v-model="formData.raca_id" 
          required 
          class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200"
        >
          <option disabled value="">Selecione a raça do seu pet</option>
          <option v-for="raca in racas" :key="raca.id" :value="raca.id">{{ raca.nome }}</option>
        </select>
      </div>

      <!-- Pet Preview -->
      <div v-if="formData.nome" class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-4 border border-green-200/50">
        <h3 class="text-sm font-semibold text-green-700 mb-2 flex items-center space-x-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
          </svg>
          <span>Pré-visualização</span>
        </h3>
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center">
            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
          <div>
            <p class="font-semibold text-gray-900">{{ formData.nome }}</p>
            <p class="text-sm text-gray-600">{{ getRacaNome(formData.raca_id) || 'Raça não selecionada' }}</p>
          </div>
        </div>
      </div>
      
      <div class="flex justify-end space-x-4 pt-4">
        <button 
          type="button" 
          @click="$emit('close')" 
          class="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
        >
          Cancelar
        </button>
        <button 
          type="submit" 
          :disabled="!isFormValid"
          class="px-6 py-3 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 transform hover:scale-105 transition-all duration-200 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
        >
          <span class="flex items-center space-x-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
            <span>Adicionar Pet</span>
          </span>
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';

const { successCreate } = useSuccessMessage();
const { showError } = useErrorMessage();

const props = defineProps({
  racas: {
    type: Array,
    default: () => []
  }
});

const emit = defineEmits(['add-pet', 'close']);

const formData = ref({
  nome: '',
  data_nascimento: '',
  raca_id: ''
});

// Data máxima permitida (hoje).
const maxDate = computed(() => {
  const today = new Date();
  return today.toISOString().split('T')[0];
});

// Verifica se a data de nascimento é válida (não é no futuro).
const isDateValid = computed(() => {
  // Se não há data selecionada, considera inválido (data é obrigatória)
  if (!formData.value.data_nascimento || formData.value.data_nascimento.trim() === '') {
    return false;
  }
  const selectedDate = new Date(formData.value.data_nascimento);
  const today = new Date();
  today.setHours(23, 59, 59, 999); // Permite até o final do dia atual
  return selectedDate <= today;
});

// Mostra validação da data sempre
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
  return formData.value.nome.trim() && formData.value.raca_id && isDateValid.value;
});


const getDateValidationMessage = () => {
  if (!formData.value.data_nascimento || formData.value.data_nascimento.trim() === '') {
    return 'A data de nascimento é obrigatória';
  }
  
  const selectedDate = new Date(formData.value.data_nascimento);
  const today = new Date();
  today.setHours(23, 59, 59, 999);
  
  if (selectedDate > today) {
    return 'A data de nascimento não pode ser uma data futura';
  }
  
  return 'Data válida';
};


const getRacaNome = (racaId) => {
  const raca = props.racas.find(r => r.id === racaId);
  return raca ? raca.nome : '';
};


const submitForm = async () => {
  if (!formData.value.nome.trim()) {
    showError('O nome do pet é obrigatório.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!formData.value.raca_id) {
    showError('A raça do pet é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!formData.value.data_nascimento || formData.value.data_nascimento.trim() === '') {
    showError('A data de nascimento é obrigatória.', { title: 'Campo Obrigatório' });
    return;
  }
  
  if (!isDateValid.value) {
    showError('A data de nascimento não pode ser no futuro.', { title: 'Data Inválida' });
    return;
  }
  
  emit('add-pet', { ...formData.value });
  
  formData.value = {
    nome: '',
    data_nascimento: '',
    raca_id: ''
  };

  successCreate('Pet');
};
</script>
