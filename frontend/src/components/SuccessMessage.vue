<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 translate-y-2 scale-95"
      enter-to-class="opacity-100 translate-y-0 scale-100"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 scale-100"
      leave-to-class="opacity-0 translate-y-2 scale-95"
    >
      <div
        v-if="visible"
        class="fixed top-4 right-4 z-50 max-w-sm w-full"
      >
        <div class="bg-white rounded-xl shadow-2xl border border-gray-100 overflow-hidden">
          <!-- Header com gradiente -->
          <div class="bg-gradient-to-r from-green-500 to-emerald-500 px-4 py-2">
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-2">
                <div class="w-6 h-6 bg-white/20 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                </div>
                <h3 class="text-white font-semibold text-sm">{{ title || 'Sucesso!' }}</h3>
              </div>
              <button
                @click="close"
                class="text-white/80 hover:text-white transition-colors duration-200 p-1"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
              </button>
            </div>
          </div>
          
          <!-- Conteúdo -->
          <div class="p-4">
            <p class="text-gray-700 text-sm leading-relaxed">{{ message }}</p>
          </div>
          
          <!-- Barra de progresso -->
          <div class="h-1 bg-gray-100">
            <div 
              class="h-full bg-gradient-to-r from-green-500 to-emerald-500 transition-all duration-100 ease-linear"
              :style="{ width: `${progress}%` }"
            ></div>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const props = defineProps({
  message: {
    type: String,
    required: true
  },
  title: {
    type: String,
    default: 'Sucesso!'
  },
  duration: {
    type: Number,
    default: 4000
  },
  autoClose: {
    type: Boolean,
    default: true
  }
});

const emit = defineEmits(['close']);

const visible = ref(true);
const progress = ref(100);
let progressInterval = null;
let closeTimeout = null;


//Fecha a mensagem
const close = () => {
  visible.value = false;
  clearInterval(progressInterval);
  clearTimeout(closeTimeout);
  
  // Aguarda a animação de saída antes de emitir o evento
  setTimeout(() => {
    emit('close');
  }, 200);
};

//Inicia o timer de auto-fechamento
const startAutoClose = () => {
  if (!props.autoClose) return;
  
  const startTime = Date.now();
  const updateInterval = 50;
  
  progressInterval = setInterval(() => {
    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, props.duration - elapsed);
    progress.value = (remaining / props.duration) * 100;
    
    if (remaining <= 0) {
      close();
    }
  }, updateInterval);
};

onMounted(() => {
  startAutoClose();
});

onUnmounted(() => {
  clearInterval(progressInterval);
  clearTimeout(closeTimeout);
});
</script>
