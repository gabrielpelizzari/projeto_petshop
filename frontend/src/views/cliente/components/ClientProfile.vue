<template>
  <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-6 border border-gray-100 shadow-lg">

    <!-- Formulário de Edição -->
    <div v-if="isEditing" class="space-y-6">
      <!-- Header do Formulário -->
      <div class="flex items-center justify-between pb-4 border-b border-gray-200">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-500 rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
            </svg>
          </div>
          <div>
            <h3 class="text-lg font-semibold text-gray-900">Editando Perfil</h3>
            <p class="text-sm text-gray-600">Atualize suas informações pessoais</p>
          </div>
        </div>
        <button 
          type="button" 
          @click="cancelEdit" 
          class="p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-lg transition-colors duration-200"
          title="Cancelar edição"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <form @submit.prevent="saveProfile" class="space-y-8">
        <!-- Seção: Dados Pessoais -->
        <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
          <div class="px-6 py-4 border-b border-gray-100">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center">
                <svg class="w-4 h-4 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900">Dados Pessoais</h4>
                <p class="text-sm text-gray-600">Informações básicas do seu perfil</p>
              </div>
            </div>
          </div>
          <div class="p-6 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label for="cliente-nome" class="block text-sm font-medium text-gray-700">
                  Nome *
                </label>
                <input 
                  type="text" 
                  id="cliente-nome" 
                  v-model="formattedNome" 
                  required 
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                  placeholder="Seu nome"
                >
              </div>
              <div class="space-y-2">
                <label for="cliente-sobrenome" class="block text-sm font-medium text-gray-700">
                  Sobrenome *
                </label>
                <input 
                  type="text" 
                  id="cliente-sobrenome" 
                  v-model="formattedSobrenome" 
                  required 
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                  placeholder="Seu sobrenome"
                >
              </div>
            </div>
            
            <div class="space-y-2">
              <label for="cliente-cpf" class="block text-sm font-medium text-gray-700">
                CPF
              </label>
              <input 
                type="text" 
                id="cliente-cpf" 
                :value="formatCpf(cliente?.cpf)" 
                disabled 
                class="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-lg cursor-not-allowed text-gray-500"
              >
              <p class="text-xs text-gray-500">O CPF não pode ser alterado</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label for="cliente-nova-senha" class="block text-sm font-medium text-gray-700">
                  Nova Senha
                </label>
                <input 
                  type="password" 
                  id="cliente-nova-senha" 
                  v-model="editData.nova_senha" 
                  placeholder="Digite a nova senha"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                >
              </div>
              <div class="space-y-2">
                <label for="cliente-confirma-senha" class="block text-sm font-medium text-gray-700">
                  Confirmar Nova Senha
                </label>
                <input 
                  type="password" 
                  id="cliente-confirma-senha" 
                  v-model="editData.confirma_nova_senha" 
                  placeholder="Confirme a nova senha"
                  :class="[
                    'w-full px-4 py-3 border rounded-lg focus:ring-2 transition-colors duration-200',
                    passwordsMatch ? 'border-gray-300 focus:ring-blue-500 focus:border-blue-500' : 'border-red-300 focus:ring-red-500 focus:border-red-500'
                  ]"
                >
              </div>
            </div>
            
            <!-- Feedback de validação de senha -->
            <div v-if="editData.nova_senha || editData.confirma_nova_senha" class="space-y-2">
              <div v-if="!passwordsMatch && editData.confirma_nova_senha" class="flex items-center space-x-2 text-red-600">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <span class="text-sm">As senhas não coincidem</span>
              </div>
              <div v-else-if="passwordsMatch && editData.nova_senha && editData.confirma_nova_senha" class="flex items-center space-x-2 text-green-600">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span class="text-sm">Senhas coincidem</span>
              </div>
              <p class="text-xs text-gray-500">Opcional - preencha apenas se desejar alterar a senha</p>
            </div>
          </div>
        </div>

        <!-- Seção: Contatos -->
        <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
          <div class="px-6 py-4 border-b border-gray-100">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-green-100 rounded-lg flex items-center justify-center">
                <svg class="w-4 h-4 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 4.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900">Informações de Contato</h4>
                <p class="text-sm text-gray-600">Como podemos entrar em contato com você</p>
              </div>
            </div>
          </div>
          <div class="p-6 space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label for="cliente-email" class="block text-sm font-medium text-gray-700">
                  Email *
                </label>
                <input 
                  type="email" 
                  id="cliente-email" 
                  v-model="editData.email" 
                  required 
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                  placeholder="seu@email.com"
                >
              </div>
              <div class="space-y-2">
                <label for="cliente-telefone" class="block text-sm font-medium text-gray-700">
                  Telefone *
                </label>
                <input 
                  type="tel" 
                  id="cliente-telefone" 
                  v-model="formattedTelefone" 
                  required 
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                  placeholder="(00) 00000-0000"
                >
              </div>
            </div>
          </div>
        </div>

        <!-- Seção: Endereço -->
        <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
          <div class="px-6 py-4 border-b border-gray-100">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div>
                <h4 class="font-semibold text-gray-900">Endereço Principal</h4>
                <p class="text-sm text-gray-600">Seu endereço de correspondência</p>
              </div>
            </div>
          </div>
          <div class="p-6 space-y-6">
            <div class="space-y-2">
              <label for="endereco-logradouro" class="block text-sm font-medium text-gray-700">
                Logradouro *
              </label>
              <input 
                type="text" 
                id="endereco-logradouro" 
                v-model="editData.endereco.logradouro" 
                required 
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                placeholder="Rua, Avenida, etc."
              >
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label for="endereco-cidade" class="block text-sm font-medium text-gray-700">
                  Cidade *
                </label>
                <input 
                  type="text" 
                  id="endereco-cidade" 
                  v-model="editData.endereco.cidade" 
                  required 
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                  placeholder="Nome da cidade"
                >
              </div>
              <div class="space-y-2">
                <label for="endereco-bairro" class="block text-sm font-medium text-gray-700">
                  Bairro *
                </label>
                <input 
                  type="text" 
                  id="endereco-bairro" 
                  v-model="editData.endereco.bairro" 
                  required 
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                  placeholder="Nome do bairro"
                >
              </div>
            </div>

            <div class="space-y-2">
              <label for="endereco-complemento" class="block text-sm font-medium text-gray-700">
                Complemento
              </label>
              <input 
                type="text" 
                id="endereco-complemento" 
                v-model="editData.endereco.complemento" 
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-200"
                placeholder="Apartamento, bloco, etc. (opcional)"
              >
            </div>
          </div>
        </div>

        <!-- Botões de Ação -->
        <div class="flex justify-end space-x-4 pt-6 border-t border-gray-200">
          <button 
            type="button" 
            @click="cancelEdit" 
            class="px-6 py-3 text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200 font-medium"
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            :disabled="!passwordsMatch"
            :class="[
              'px-8 py-3 font-semibold rounded-lg transition-all duration-200 shadow-lg',
              passwordsMatch 
                ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 hover:shadow-xl' 
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            ]"
          >
            <span class="flex items-center space-x-2">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
              <span>Salvar Alterações</span>
            </span>
          </button>
        </div>
      </form>
    </div>

    <!-- Exibição dos Dados -->
    <div v-else class="space-y-6">
      <!-- Header com botão de editar -->
      <div class="flex justify-between items-center pb-4 border-b border-gray-200">
        <div>
          <h3 class="text-lg font-semibold text-gray-900">Informações Pessoais</h3>
          <p class="text-sm text-gray-600">Visualize e gerencie seus dados</p>
        </div>
        <button 
          @click="startEdit"
          class="px-4 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-medium rounded-xl hover:from-blue-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
        >
          <span class="flex items-center space-x-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
            </svg>
            <span>Editar Perfil</span>
          </span>
        </button>
      </div>
      <!-- Dados Pessoais -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gradient-to-r from-blue-50 to-blue-100 rounded-xl p-4">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
            </div>
            <div>
              <p class="text-sm text-blue-600 font-medium">Nome</p>
              <p class="text-lg font-semibold text-gray-900">{{ cliente?.nome || 'Não informado' }}</p>
            </div>
          </div>
        </div>
        <div class="bg-gradient-to-r from-purple-50 to-purple-100 rounded-xl p-4">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-purple-500 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
            </div>
            <div>
              <p class="text-sm text-purple-600 font-medium">CPF</p>
              <p class="text-lg font-semibold text-gray-900">{{ formatCpf(cliente?.cpf) || 'Não informado' }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Contatos -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gradient-to-r from-green-50 to-green-100 rounded-xl p-4">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"/>
              </svg>
            </div>
            <div>
              <p class="text-sm text-green-600 font-medium">Email</p>
              <p class="text-lg font-semibold text-gray-900">{{ getEmailPrincipal() || 'Não informado' }}</p>
            </div>
          </div>
        </div>
        <div class="bg-gradient-to-r from-yellow-50 to-yellow-100 rounded-xl p-4">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-yellow-500 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
            </div>
            <div>
              <p class="text-sm text-yellow-600 font-medium">Telefone</p>
              <p class="text-lg font-semibold text-gray-900">{{ getTelefonePrincipal() || 'Não informado' }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Endereço -->
      <div class="bg-gradient-to-r from-indigo-50 to-indigo-100 rounded-xl p-4">
        <div class="flex items-start space-x-3">
          <div class="w-10 h-10 bg-indigo-500 rounded-lg flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </div>
          <div class="flex-1">
            <p class="text-sm text-indigo-600 font-medium">Endereço Principal</p>
            <p class="text-lg font-semibold text-gray-900">{{ getEnderecoPrincipal() || 'Não informado' }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Formulário de Troca de Senha -->
    <div v-if="showPasswordForm" class="mt-6 bg-gradient-to-r from-yellow-50 to-orange-50 rounded-xl p-6 border border-yellow-200/50">
      <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center space-x-2">
        <svg class="w-5 h-5 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
        </svg>
        <span>Alterar Senha</span>
      </h3>
      <form @submit.prevent="changePassword" class="space-y-4">
        <div>
          <label for="senha-antiga" class="block text-sm font-semibold text-gray-700 mb-2">Senha Atual</label>
          <input 
            type="password" 
            id="senha-antiga" 
            v-model="passwordData.senha_antiga" 
            required 
            class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-500/20 focus:border-yellow-500 transition-all duration-200"
          >
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label for="nova-senha" class="block text-sm font-semibold text-gray-700 mb-2">Nova Senha</label>
            <input 
              type="password" 
              id="nova-senha" 
              v-model="passwordData.nova_senha" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-500/20 focus:border-yellow-500 transition-all duration-200"
            >
          </div>
          <div>
            <label for="confirma-nova-senha" class="block text-sm font-semibold text-gray-700 mb-2">Confirmar Nova Senha</label>
            <input 
              type="password" 
              id="confirma-nova-senha" 
              v-model="passwordData.confirma_nova_senha" 
              required 
              class="w-full px-4 py-3 bg-white/80 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-yellow-500/20 focus:border-yellow-500 transition-all duration-200"
            >
          </div>
        </div>
        <div class="flex justify-end space-x-3 pt-4">
          <button 
            type="button" 
            @click="showPasswordForm = false" 
            class="px-4 py-2 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors duration-200 font-medium"
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            class="px-6 py-2 bg-gradient-to-r from-yellow-600 to-orange-600 text-white font-semibold rounded-xl hover:from-yellow-700 hover:to-orange-700 transform hover:scale-105 transition-all duration-200 shadow-lg"
          >
            Confirmar Alteração
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue';
import { useCharacterOnlyFormatter } from '@/composables/useCharacterOnlyFormatter';
import { usePhoneFormatter } from '@/composables/usePhoneFormatter';
import { useCpfFormatter } from '@/composables/useCpfFormatter';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';

const props = defineProps({
  cliente: {
    type: Object,
    default: () => ({})
  }
});

const emit = defineEmits(['update-profile', 'change-password']);

const isEditing = ref(false);
const showPasswordForm = ref(false);
const editData = ref({});

const { showError } = useErrorMessage();

const { text: formattedNome } = useCharacterOnlyFormatter();
const { text: formattedSobrenome } = useCharacterOnlyFormatter();
const { phone: formattedTelefone } = usePhoneFormatter();
const { formatCpf } = useCpfFormatter();
const passwordData = ref({
  senha_antiga: '',
  nova_senha: '',
  confirma_nova_senha: ''
});

watch(formattedNome, (newValue) => { editData.value.nome = newValue; });
watch(formattedSobrenome, (newValue) => { editData.value.sobrenome = newValue; });
watch(formattedTelefone, (newValue) => { editData.value.telefone = newValue.replace(/\D/g, ''); });

const passwordsMatch = computed(() => {
  if (!editData.value.nova_senha && !editData.value.confirma_nova_senha) return true;
  return editData.value.nova_senha === editData.value.confirma_nova_senha;
});


const startEdit = () => {
  const [nome, ...sobrenomeParts] = (props.cliente.nome || '').split(' ');
  
  editData.value = {
    nome: nome || '',
    sobrenome: sobrenomeParts.join(' ') || '',
    nova_senha: '',
    confirma_nova_senha: '',
    email: '',
    telefone: '',
    endereco: {
      logradouro: '',
      cidade: '',
      bairro: '',
      complemento: '',
      tag: 'Principal'
    }
  };
  
  // Preenche dados de contato se existirem
  const emailPrincipal = props.cliente.contatos?.find(c => c.tipo === 'email' && c.tag === 'Principal');
  if (emailPrincipal) editData.value.email = emailPrincipal.valor;
  
  const telefonePrincipal = props.cliente.contatos?.find(c => c.tipo === 'telefone' && c.tag === 'Principal');
  if (telefonePrincipal) formattedTelefone.value = telefonePrincipal.valor;
  
  // Preenche dados de endereço se existir
  if (props.cliente.enderecos && props.cliente.enderecos.length > 0) {
    const enderecoPrincipal = props.cliente.enderecos[0];
    editData.value.endereco = { ...enderecoPrincipal };
  }
  
  // Define os valores formatados
  formattedNome.value = editData.value.nome;
  formattedSobrenome.value = editData.value.sobrenome;
  
  isEditing.value = true;
};

const cancelEdit = () => {
  isEditing.value = false;
  editData.value = {};
};


const saveProfile = () => {
  // Valida se as senhas coincidem (se foram preenchidas)
  if ((editData.value.nova_senha || editData.value.confirma_nova_senha) && !passwordsMatch.value) {
    showError('As senhas não coincidem. Por favor, verifique e tente novamente.', { title: 'Senha Inválida' });
    return;
  }
  
  // Remove o campo de confirmação antes de enviar
  const dataToSave = { ...editData.value };
  delete dataToSave.confirma_nova_senha;
  
  emit('update-profile', dataToSave);
  isEditing.value = false;
};


const changePassword = () => {
  if (passwordData.value.nova_senha !== passwordData.value.confirma_nova_senha) {
    showError('As senhas não coincidem!', { title: 'Senha Inválida' });
    return;
  }
  
  emit('change-password', passwordData.value);
  showPasswordForm.value = false;
  passwordData.value = {
    senha_antiga: '',
    nova_senha: '',
    confirma_nova_senha: ''
  };
};

// Obtém o email principal do cliente.
const getEmailPrincipal = () => {
  const emailPrincipal = props.cliente.contatos?.find(c => c.tipo === 'email' && c.tag === 'Principal');
  return emailPrincipal?.valor || '';
};

// Obtém o telefone principal do cliente formatado.
const getTelefonePrincipal = () => {
  const telefonePrincipal = props.cliente.contatos?.find(c => c.tipo === 'telefone' && c.tag === 'Principal');
  if (telefonePrincipal?.valor) {
    const { formatPhone } = usePhoneFormatter();
    return formatPhone(telefonePrincipal.valor);
  }
  return '';
};

// Obtém o endereço principal formatado.
const getEnderecoPrincipal = () => {
  if (props.cliente.enderecos && props.cliente.enderecos.length > 0) {
    const endereco = props.cliente.enderecos[0];
    const partes = [endereco.logradouro, endereco.bairro, endereco.cidade].filter(Boolean);
    return partes.join(', ');
  }
  return '';
};
</script>
