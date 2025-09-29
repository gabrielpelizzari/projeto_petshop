<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-50 flex items-center justify-center p-4">
    <!-- Decorative Elements -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-20 h-20 bg-blue-200/30 rounded-full blur-xl"></div>
      <div class="absolute top-40 right-20 w-32 h-32 bg-green-200/30 rounded-full blur-xl"></div>
      <div class="absolute bottom-20 left-1/4 w-24 h-24 bg-purple-200/30 rounded-full blur-xl"></div>
    </div>

    <!-- Login Container -->
    <div class="relative w-full max-w-md">
      <!-- Header with Logo -->
      <div class="text-center mb-8">
        <RouterLink to="/" class="inline-flex items-center space-x-2 group">
          <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-green-500 rounded-xl flex items-center justify-center group-hover:scale-105 transition-transform duration-200">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
              <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
              <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
            </svg>
          </div>
          <span class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">
            PetHub
          </span>
        </RouterLink>
        <h1 class="mt-6 text-3xl font-bold text-gray-900">Bem-vindo de volta</h1>
        <p class="mt-2 text-gray-600">Entre na sua conta para continuar</p>
      </div>

      <!-- Login Form -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-8 border border-gray-100 shadow-xl">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- CPF Field -->
          <div class="space-y-2">
            <label for="cpf" class="block text-sm font-semibold text-gray-700">
              CPF
            </label>
            <div class="relative">
              <input
                id="cpf"
                v-model="formattedCpf"
                type="text"
                required
                placeholder="000.000.000-00"
                class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400"
              />
              <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Password Field -->
          <div class="space-y-2">
            <label for="password" class="block text-sm font-semibold text-gray-700">
              Senha
            </label>
            <div class="relative">
              <input
                id="password"
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                required
                placeholder="Digite sua senha"
                class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400 pr-12"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 transition-colors duration-200"
              >
                <svg v-if="!showPassword" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                </svg>
                <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.878 9.878L3 3m6.878 6.878L21 21"/>
                </svg>
              </button>
            </div>
          </div>


          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="w-full px-6 py-3 bg-gradient-to-r from-blue-600 to-green-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-green-700 focus:outline-none focus:ring-2 focus:ring-blue-500/20 disabled:opacity-50 disabled:cursor-not-allowed transform hover:scale-[1.02] transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            <span v-if="loading" class="flex items-center justify-center space-x-2">
              <svg class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Entrando...</span>
            </span>
            <span v-else>Entrar na conta</span>
          </button>
        </form>

        <!-- Footer Links -->
        <div class="mt-6 text-center space-y-4">
          <div class="text-sm text-gray-600">
            Não tem uma conta?
            <RouterLink 
              to="/cadastro" 
              class="font-semibold text-blue-600 hover:text-blue-700 transition-colors duration-200"
            >
              Cadastre-se aqui
            </RouterLink>
          </div>
          
          <div class="pt-4 border-t border-gray-200">
            <RouterLink 
              to="/" 
              class="text-sm text-gray-500 hover:text-gray-700 transition-colors duration-200 flex items-center justify-center space-x-1"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
              </svg>
              <span>Voltar ao início</span>
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, reactive } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useCpfFormatter } from '@/composables/useCpfFormatter';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';


const { showSuccess } = useSuccessMessage();
const { showError } = useErrorMessage();

const { cpf: formattedCpf } = useCpfFormatter();

watch(formattedCpf, (newValue) => {
  credenciais.cpf = newValue.replace(/\D/g, '');
});

const credenciais = reactive({
  cpf: '',
})

const password = ref('');
const loading = ref(false);
const showPassword = ref(false);

const authStore = useAuthStore();
const router = useRouter();


const handleLogin = async () => {
  loading.value = true;
  
  try {
    const success = await authStore.login(credenciais.cpf, password.value);
    
    if (success) {
      showSuccess('Login realizado com sucesso!');
      router.push('/dashboard');
    } else {
      showError('CPF ou senha inválidos. Verifique suas credenciais e tente novamente.', { title: 'Credenciais Inválidas' });
    }
  } catch (err) {
    console.error('Erro no login:', err);
    showError('Erro ao conectar com o servidor. Tente novamente em alguns instantes.', { title: 'Erro de Conexão' });
  } finally {
    loading.value = false;
  }
};
</script>
