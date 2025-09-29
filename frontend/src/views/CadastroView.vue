<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-50 flex items-center justify-center p-4">
    <!-- Decorative Elements -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-20 h-20 bg-blue-200/30 rounded-full blur-xl"></div>
      <div class="absolute top-40 right-20 w-32 h-32 bg-green-200/30 rounded-full blur-xl"></div>
      <div class="absolute bottom-20 left-1/4 w-24 h-24 bg-purple-200/30 rounded-full blur-xl"></div>
    </div>

    <!-- Cadastro Container -->
    <div class="relative w-full max-w-2xl">
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
        <h1 class="mt-6 text-3xl font-bold text-gray-900">Criar sua conta</h1>
        <p class="mt-2 text-gray-600">Junte-se à nossa comunidade pet</p>
      </div>

      <!-- Cadastro Form -->
      <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-8 border border-gray-100 shadow-xl">
        <form @submit.prevent="handleCadastro" class="space-y-6">
          <!-- Dados Pessoais -->
          <div class="space-y-4">
            <h3 class="text-lg font-semibold text-gray-900 border-b border-gray-200 pb-2">
              Dados Pessoais
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Nome -->
              <div class="space-y-2">
                <label for="nome" class="block text-sm font-semibold text-gray-700">
                  Nome *
                </label>
                <div class="relative">
                  <input
                    id="nome"
                    v-model="formattedNome"
                    type="text"
                    required
                    placeholder="Seu nome"
                    class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400"
                  />
                </div>
              </div>

              <!-- Sobrenome -->
              <div class="space-y-2">
                <label for="sobrenome" class="block text-sm font-semibold text-gray-700">
                  Sobrenome *
                </label>
                <div class="relative">
                  <input
                    id="sobrenome"
                    v-model="formattedSobrenome"
                    type="text"
                    required
                    placeholder="Seu sobrenome"
                    class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400"
                  />
                </div>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Email -->
              <div class="space-y-2">
                <label for="email" class="block text-sm font-semibold text-gray-700">Email *</label>
                <input id="email" v-model="formData.email" type="email" required placeholder="seu@email.com" class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400">
              </div>

              <!-- Telefone -->
              <div class="space-y-2">
                <label for="telefone" class="block text-sm font-semibold text-gray-700">Telefone *</label>
                <input id="telefone" v-model="formattedTelefone" type="tel" required placeholder="(00) 00000-0000" class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all duration-200 placeholder-gray-400">
              </div>
            </div>

            <!-- CPF -->
            <div class="space-y-2">
              <label for="cpf" class="block text-sm font-semibold text-gray-700">
                CPF *
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

            <!-- Senha -->
            <div class="space-y-2">
              <label for="senha" class="block text-sm font-semibold text-gray-700">
                Senha *
              </label>
              <div class="relative">
                <input
                  id="senha"
                  v-model="formData.senha"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  placeholder="Digite sua senha (mín. 6 caracteres)"
                  :class="[
                    'w-full px-4 py-3 bg-white/80 border rounded-xl focus:outline-none focus:ring-2 transition-all duration-200 placeholder-gray-400 pr-12',
                    passwordStrengthClass
                  ]"
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
              <!-- Mensagem de validação da senha -->
              <div v-if="showPasswordStrength" class="text-sm flex items-center space-x-2">
                <svg v-if="passwordIsValid" class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <svg v-else class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span :class="passwordIsValid ? 'text-green-600' : 'text-red-600'">
                  {{ passwordIsValid ? 'Senha válida' : 'Senha deve ter pelo menos 6 caracteres' }}
                </span>
              </div>
            </div>

            <!-- Confirmar Senha -->
            <div class="space-y-2">
              <label for="confirma_senha" class="block text-sm font-semibold text-gray-700">
                Confirmar Senha *
              </label>
              <div class="relative">
                <input
                  id="confirma_senha"
                  v-model="formData.confirma_senha"
                  type="password"
                  required
                  placeholder="Confirme sua senha"
                  :class="[
                    'w-full px-4 py-3 bg-white/80 border rounded-xl focus:outline-none focus:ring-2 transition-all duration-200 placeholder-gray-400 pr-12',
                    passwordValidationClass
                  ]"
                />
                <!-- Ícone de validação -->
                <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                  <svg v-if="showPasswordValidation && passwordsMatch" class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  <svg v-else-if="showPasswordValidation && !passwordsMatch" class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                  </svg>
                </div>
              </div>
              <!-- Mensagem de validação -->
              <div v-if="showPasswordValidation" class="text-sm flex items-center space-x-2">
                <svg v-if="passwordsMatch" class="w-4 h-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <svg v-else class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span :class="passwordsMatch ? 'text-green-600' : 'text-red-600'">
                  {{ passwordsMatch ? 'Senhas coincidem' : 'As senhas não coincidem' }}
                </span>
              </div>
            </div>
          </div>

          <!-- Endereço -->
          <div class="space-y-4">
            <h3 class="text-lg font-semibold text-gray-900 border-b border-gray-200 pb-2">
              Endereço
            </h3>
            
            <!-- Logradouro -->
            <div class="space-y-2">
              <label for="logradouro" class="block text-sm font-semibold text-gray-700">
                Logradouro *
              </label>
              <div class="relative">
                <input
                  id="logradouro"
                  v-model="formData.endereco.logradouro"
                  type="text"
                  required
                  placeholder="Rua, Avenida, etc."
                  class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
                />
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Cidade -->
              <div class="space-y-2">
                <label for="cidade" class="block text-sm font-semibold text-gray-700">
                  Cidade *
                </label>
                <div class="relative">
                  <input
                    id="cidade"
                    v-model="formData.endereco.cidade"
                    type="text"
                    required
                    placeholder="Sua cidade"
                    class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
                  />
                </div>
              </div>

              <!-- Bairro -->
              <div class="space-y-2">
                <label for="bairro" class="block text-sm font-semibold text-gray-700">
                  Bairro *
                </label>
                <div class="relative">
                  <input
                    id="bairro"
                    v-model="formData.endereco.bairro"
                    type="text"
                    required
                    placeholder="Seu bairro"
                    class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
                  />
                </div>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Complemento -->
              <div class="space-y-2">
                <label for="complemento" class="block text-sm font-semibold text-gray-700">
                  Complemento
                </label>
                <div class="relative">
                  <input
                    id="complemento"
                    v-model="formData.endereco.complemento"
                    type="text"
                    placeholder="Apto, casa, etc."
                    class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
                  />
                </div>
              </div>

              <!-- Tag -->
              <div class="space-y-2">
                <label for="tag" class="block text-sm font-semibold text-gray-700">
                  Tag
                </label>
                <div class="relative">
                  <input
                    id="tag"
                    v-model="formData.endereco.tag"
                    type="text"
                    placeholder="Casa, trabalho, etc."
                    class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500/20 focus:border-green-500 transition-all duration-200 placeholder-gray-400"
                  />
                </div>
              </div>
            </div>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="p-4 bg-red-50 border border-red-200 rounded-xl">
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <p class="text-sm text-red-700 font-medium">{{ error }}</p>
            </div>
          </div>

          <!-- Success Message -->
          <div v-if="success" class="p-4 bg-green-50 border border-green-200 rounded-xl">
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
              <p class="text-sm text-green-700 font-medium">{{ success }}</p>
            </div>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading || !passwordsMatch || !passwordIsValid"
            :class="[
              'w-full px-6 py-3 font-semibold rounded-xl focus:outline-none focus:ring-2 transform transition-all duration-200 shadow-lg',
              (loading || !passwordsMatch || !passwordIsValid) 
                ? 'bg-gray-400 cursor-not-allowed opacity-50' 
                : 'bg-gradient-to-r from-blue-600 to-green-600 text-white hover:from-blue-700 hover:to-green-700 focus:ring-blue-500/20 hover:scale-[1.02] hover:shadow-xl'
            ]"
          >
            <span v-if="loading" class="flex items-center justify-center space-x-2">
              <svg class="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span>Criando conta...</span>
            </span>
            <span v-else>Criar conta</span>
          </button>
        </form>

        <!-- Footer Links -->
        <div class="mt-6 text-center space-y-4">
          <div class="text-sm text-gray-600">
            Já tem uma conta?
            <RouterLink 
              to="/login" 
              class="font-semibold text-blue-600 hover:text-blue-700 transition-colors duration-200"
            >
              Faça login aqui
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

    <!-- Componentes de Confirmação -->
    <ConfirmationContainer />
  </div>
</template>

<script setup>
import { ref, reactive, watch, computed } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useCpfFormatter } from '@/composables/useCpfFormatter';
import { useCharacterOnlyFormatter } from '@/composables/useCharacterOnlyFormatter';
import { usePhoneFormatter } from '@/composables/usePhoneFormatter';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';
import { useAuthStore } from '@/stores/auth';
import ConfirmationContainer from '@/components/ConfirmationContainer.vue';
import api from '@/services/api';

// Composables
const router = useRouter();
const { successCreate } = useSuccessMessage();
const { showError, showApiError } = useErrorMessage();
const { showConfirmation } = useConfirmation();

const { cpf: formattedCpf } = useCpfFormatter();
const { text: formattedNome } = useCharacterOnlyFormatter();
const { text: formattedSobrenome } = useCharacterOnlyFormatter();
const { phone: formattedTelefone } = usePhoneFormatter();

// Estados
const loading = ref(false);
const error = ref(null);
const success = ref(null);
const showPassword = ref(false);

// Dados do formulário
const formData = reactive({
  nome: '',
  sobrenome: '',
  cpf: '',
  senha: '',
  confirma_senha: '',
  email: '',
  telefone: '',
  endereco: {
    logradouro: '',
    cidade: '',
    bairro: '',
    complemento: '',
    tag: ''
  }
});


const passwordsMatch = computed(() => {
  if (!formData.senha && !formData.confirma_senha) return true;
  return formData.senha === formData.confirma_senha;
});

const passwordIsValid = computed(() => {
  return formData.senha.length >= 6;
});

const showPasswordValidation = computed(() => {
  return formData.confirma_senha.length > 0;
});

const showPasswordStrength = computed(() => {
  return formData.senha.length > 0;
});

const passwordValidationClass = computed(() => {
  if (!showPasswordValidation.value) {
    return 'border-gray-200 focus:border-blue-500 focus:ring-blue-500/20';
  }
  
  return passwordsMatch.value 
    ? 'border-green-300 focus:border-green-500 focus:ring-green-500/20'
    : 'border-red-300 focus:border-red-500 focus:ring-red-500/20';
});

const passwordStrengthClass = computed(() => {
  if (!showPasswordStrength.value) {
    return 'border-gray-200 focus:border-blue-500 focus:ring-blue-500/20';
  }
  
  return passwordIsValid.value 
    ? 'border-green-300 focus:border-green-500 focus:ring-green-500/20'
    : 'border-red-300 focus:border-red-500 focus:ring-red-500/20';
});

watch(formattedNome, (newValue) => { formData.nome = newValue; });
watch(formattedSobrenome, (newValue) => { formData.sobrenome = newValue; });
watch(formattedCpf, (newValue) => { formData.cpf = newValue.replace(/\D/g, ''); });
watch(formattedTelefone, (newValue) => { formData.telefone = newValue.replace(/\D/g, ''); });

const handleCadastro = async () => {
  if (!passwordsMatch.value) {
    showError('As senhas não coincidem. Por favor, verifique e tente novamente.', { title: 'Senha Inválida' });
    return;
  }

  // Validação de tamanho da senha
  if (formData.senha.length < 6) {
    showError('A senha deve ter pelo menos 6 caracteres.', { title: 'Senha Muito Curta' });
    return;
  }

  // Verifica se já existe uma sessão ativa
  const authStore = useAuthStore();
  if (authStore.isAuthenticated) {
    const confirmar = await showConfirmation(
      `Já existe uma conta logada (${authStore.usuario?.nome}). Deseja sair da conta atual e continuar com o cadastro?`,
      {
        title: 'Sessão Ativa Detectada',
        confirmText: 'Sair e Continuar',
        cancelText: 'Cancelar Cadastro',
        variant: 'primary'
      }
    );
    
    if (!confirmar) {
      return; // Usuário cancelou o cadastro
    }
    
    // Faz logout da conta atual
    authStore.logout();
  }

  loading.value = true;
  error.value = null;
  success.value = null;
  
  try {
    const payload = {
      nome: formData.nome.trim(),
      sobrenome: formData.sobrenome.trim(),
      cpf: formData.cpf,
      senha: formData.senha,
      email: formData.email,
      telefone: formData.telefone,
      endereco: {
        logradouro: formData.endereco.logradouro,
        cidade: formData.endereco.cidade,
        bairro: formData.endereco.bairro,
        complemento: formData.endereco.complemento || null,
        tag: formData.endereco.tag || 'Principal'
      }
    };

    await api.post('/cadastro/', payload);

    successCreate('Conta');
    
    setTimeout(() => {
      router.push('/login');
    }, 2000);

  } catch (err) {
    console.error('Erro no cadastro:', err);
    
    if (err.response?.status === 422) {
      const validationErrors = err.response.data?.detail || [];
      
      const errorMessages = validationErrors.map(error => {
        if (error.msg?.includes('CPF deve ter exatamente 11 dígitos')) {
          return 'CPF deve ter exatamente 11 dígitos numéricos.';
        }
        if (error.msg?.includes('Senha deve ter pelo menos 6 caracteres')) {
          return 'A senha deve ter pelo menos 6 caracteres.';
        }
        if (error.msg?.includes('Nome e sobrenome não podem estar vazios')) {
          return 'Nome e sobrenome são obrigatórios.';
        }
        if (error.msg?.includes('Telefone deve ter 11 dígitos')) {
          return 'Telefone deve ter 11 dígitos.';
        }
        if (error.msg?.includes('value is not a valid email address')) {
          return 'Por favor, insira um email válido.';
        }
        if (error.msg?.includes('CPF inválido - todos os dígitos são iguais')) {
          return 'CPF inválido. Não é possível usar CPF com todos os dígitos iguais.';
        }
        
        return error.msg || 'Erro de validação nos dados informados.';
      });
      
      const firstError = errorMessages[0] || 'Verifique os dados informados e tente novamente.';
      showError(firstError, { title: 'Dados Inválidos' });
      
    } else if (err.response?.status === 400 && err.response?.data?.detail?.includes('CPF já cadastrado')) {
      showError('Este CPF já está cadastrado. Tente fazer login ou use outro CPF.', { title: 'CPF Duplicado' });
    } else if (err.response?.status === 400 && err.response?.data?.detail?.includes('E-mail já cadastrado')) {
      showError('Este email já está cadastrado. Tente fazer login ou use outro email.', { title: 'Email Duplicado' });
    } else if (err.response?.status === 400 && err.response?.data?.detail?.includes('Telefone já cadastrado')) {
      showError('Este telefone já está cadastrado. Use outro número de telefone.', { title: 'Telefone Duplicado' });
    } else {
      showApiError(err, 'Erro ao criar conta. Verifique os dados e tente novamente.');
    }
  } finally {
    loading.value = false;
  }
};
</script>