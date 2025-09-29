<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="visible"
        class="fixed inset-0 z-50 flex items-center justify-center p-4"
        @click.self="handleCancel"
      >
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black/50 backdrop-blur-sm"></div>
        
        <!-- Modal -->
        <div class="relative bg-white rounded-2xl shadow-2xl border border-gray-100 w-full max-w-md overflow-hidden">
          <!-- Header -->
          <div class="bg-gradient-to-r from-blue-500 to-purple-500 px-6 py-4">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-white">{{ title }}</h3>
            </div>
          </div>
          
          <!-- Content -->
          <div class="p-6">
            <p class="text-gray-700 leading-relaxed">{{ message }}</p>
          </div>
          
          <!-- Actions -->
          <div class="px-6 pb-6 flex justify-end space-x-3">
            <button
              @click="handleCancel"
              class="px-4 py-2 text-gray-700 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors duration-200 font-medium"
            >
              {{ cancelText }}
            </button>
            <button
              ref="confirmButton"
              @click="handleConfirm"
              :class="[
                'px-6 py-2 font-semibold rounded-lg transition-all duration-200',
                variant === 'danger' 
                  ? 'bg-gradient-to-r from-red-500 to-rose-500 hover:from-red-600 hover:to-rose-600 text-white shadow-lg hover:shadow-xl transform hover:scale-105'
                  : 'bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-600 hover:to-purple-600 text-white shadow-lg hover:shadow-xl transform hover:scale-105'
              ]"
            >
              {{ confirmText }}
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const props = defineProps({
  message: {
    type: String,
    required: true
  },
  title: {
    type: String,
    default: 'Confirmação'
  },
  confirmText: {
    type: String,
    default: 'Confirmar'
  },
  cancelText: {
    type: String,
    default: 'Cancelar'
  },
  variant: {
    type: String,
    default: 'primary', // 'primary' ou 'danger'
    validator: (value) => ['primary', 'danger'].includes(value)
  }
});

const emit = defineEmits(['confirm', 'cancel']);

const visible = ref(false);
const confirmButton = ref(null);


//Confirma a ação
const handleConfirm = () => {
  visible.value = false;
  setTimeout(() => {
    emit('confirm');
  }, 200);
};

//Cancela a ação
const handleCancel = () => {
  visible.value = false;
  setTimeout(() => {
    emit('cancel');
  }, 200);
};

// tecla ESC para cancelar
const handleKeydown = (event) => {
  if (event.key === 'Escape') {
    handleCancel();
  } else if (event.key === 'Enter') {
    handleConfirm();
  }
};

onMounted(() => {
  visible.value = true;
  document.addEventListener('keydown', handleKeydown);

  // Foca no botão de confirmar para permitir Enter imediato
  setTimeout(() => {
    if (confirmButton.value) {
      confirmButton.value.focus();
    }
  }, 100);


  return () => {
    document.removeEventListener('keydown', handleKeydown);
  };
});
</script>
