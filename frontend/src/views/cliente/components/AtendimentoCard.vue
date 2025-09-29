<template>
  <div class="bg-white/50 backdrop-blur-sm rounded-lg p-2 border border-gray-200/60 hover:bg-white/70 transition-colors duration-200">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <div class="w-6 h-6 bg-gradient-to-br from-blue-400 to-cyan-400 rounded-md flex items-center justify-center">
          <svg class="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <div class="flex-1 min-w-0">
          <p class="text-xs font-medium text-gray-800 truncate">{{ formatarDataCompacta(atendimento.data) }}</p>
          <p class="text-xs text-gray-600 truncate">{{ atendimento.descricao }}</p>
        </div>
      </div>
      <div class="text-right ml-2">
        <p class="text-xs font-bold text-blue-600">R$ {{ atendimento.valor.toFixed(2) }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  atendimento: {
    type: Object,
    required: true
  }
});

const formatarData = (dataStr) => {
  if (!dataStr) return 'Data não informada';
  
  const [ano, mes, dia] = dataStr.split('-').map(Number);
  const dataObj = new Date(ano, mes - 1, dia); // mes - 1 porque Date usa índice 0 para janeiro
  
  return new Intl.DateTimeFormat('pt-BR', {
    dateStyle: 'medium',
  }).format(dataObj);
};

const formatarDataCompacta = (dataStr) => {
  if (!dataStr) return '--/--/----';
  
  // Para evitar problemas de fuso horário
  const [ano, mes, dia] = dataStr.split('-').map(Number);
  const dataObj = new Date(ano, mes - 1, dia); // mes - 1 porque Date usa índice 0 para janeiro
  
  return new Intl.DateTimeFormat('pt-BR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  }).format(dataObj);
};
</script>
