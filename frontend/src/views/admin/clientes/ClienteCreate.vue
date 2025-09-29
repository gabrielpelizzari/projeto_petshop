<template>
  <div class="p-8 bg-gray-50 min-h-full">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Adicionar Novo Cliente</h1>

    <div class="max-w-3xl mx-auto bg-white rounded-2xl shadow-lg p-8 border border-gray-200">
      <form @submit.prevent="handleCadastro" class="space-y-8">
        <!-- Dados Pessoais -->
        <section>
          <h2 class="text-xl font-semibold text-gray-900 border-b pb-3 mb-6">Dados Pessoais</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-2">
              <label for="nome" class="block text-sm font-medium text-gray-700">Nome *</label>
              <input type="text" id="nome" v-model="formattedNome" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="sobrenome" class="block text-sm font-medium text-gray-700">Sobrenome *</label>
              <input type="text" id="sobrenome" v-model="formattedSobrenome" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="email" class="block text-sm font-medium text-gray-700">Email *</label>
              <input type="email" id="email" v-model="formData.email" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="telefone" class="block text-sm font-medium text-gray-700">Telefone *</label>
              <input type="tel" id="telefone" v-model="formattedTelefone" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="cpf" class="block text-sm font-medium text-gray-700">CPF *</label>
              <input type="text" id="cpf" v-model="formattedCpf" required placeholder="000.000.000-00" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="senha" class="block text-sm font-medium text-gray-700">Senha Provisória *</label>
              <input type="password" id="senha" v-model="formData.senha" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
          </div>
        </section>

        <!-- Endereço -->
        <section>
          <h2 class="text-xl font-semibold text-gray-900 border-b pb-3 mb-6">Endereço Principal</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-2 md:col-span-2">
              <label for="logradouro" class="block text-sm font-medium text-gray-700">Logradouro *</label>
              <input type="text" id="logradouro" v-model="formData.endereco.logradouro" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="cidade" class="block text-sm font-medium text-gray-700">Cidade *</label>
              <input type="text" id="cidade" v-model="formData.endereco.cidade" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="bairro" class="block text-sm font-medium text-gray-700">Bairro *</label>
              <input type="text" id="bairro" v-model="formData.endereco.bairro" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="complemento" class="block text-sm font-medium text-gray-700">Complemento</label>
              <input type="text" id="complemento" v-model="formData.endereco.complemento" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="tag" class="block text-sm font-medium text-gray-700">Tag</label>
              <input type="text" id="tag" v-model="formData.endereco.tag" placeholder="Ex: Principal, Casa" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
          </div>
        </section>

        <!-- Mensagens e Botão -->
        <div class="pt-6 border-t">
          <div v-if="error" class="mb-4 p-4 bg-red-100 text-red-700 rounded-lg">
            {{ error }}
          </div>
          <div v-if="success" class="mb-4 p-4 bg-green-100 text-green-700 rounded-lg">
            {{ success }}
          </div>
          <div class="flex justify-end space-x-4">
            <RouterLink to="/dashboard/admin/clientes" class="px-6 py-2 text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors">Cancelar</RouterLink>
            <button type="submit" :disabled="loading" class="px-6 py-2 font-semibold text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-blue-300 transition-colors">
              <span v-if="loading">Salvando...</span>
              <span v-else>Salvar Cliente</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useCpfFormatter } from '@/composables/useCpfFormatter';
import { useCharacterOnlyFormatter } from '@/composables/useCharacterOnlyFormatter';
import { usePhoneFormatter } from '@/composables/usePhoneFormatter';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';
import api from '@/services/api';

const router = useRouter();
const { successCreate } = useSuccessMessage();
const { showApiError } = useErrorMessage();
const { cpf: formattedCpf } = useCpfFormatter();
const { text: formattedNome } = useCharacterOnlyFormatter();
const { text: formattedSobrenome } = useCharacterOnlyFormatter();
const { phone: formattedTelefone } = usePhoneFormatter();

const loading = ref(false);
const error = ref(null);
const success = ref(null);

const formData = reactive({
  nome: '',
  sobrenome: '',
  cpf: '',
  senha: '',
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

watch(formattedNome, (newValue) => { formData.nome = newValue; });
watch(formattedSobrenome, (newValue) => { formData.sobrenome = newValue; });
watch(formattedCpf, (newValue) => { formData.cpf = newValue.replace(/\D/g, ''); });
watch(formattedTelefone, (newValue) => { formData.telefone = newValue.replace(/\D/g, ''); });

const handleCadastro = async () => {
  loading.value = true;
  error.value = null;
  success.value = null;

  try {
    await api.post('/clientes/admin', formData);
    successCreate('Cliente');
    setTimeout(() => {
      router.push('/dashboard/admin/clientes');
    }, 2000);
  } catch (err) {
    console.error('Erro ao criar cliente:', err);
    showApiError(err);
  } finally {
    loading.value = false;
  }
};
</script>
