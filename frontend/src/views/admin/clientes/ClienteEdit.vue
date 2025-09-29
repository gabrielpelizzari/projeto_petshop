<template>
  <div class="p-8 bg-gray-50 min-h-full">
    <h1 class="text-3xl font-bold text-gray-800 mb-6">Editar Cliente</h1>

    <div v-if="loading" class="text-center">
      <p>Carregando dados do cliente...</p>
    </div>

    <div v-if="error && !loading" class="max-w-3xl mx-auto p-4 bg-red-100 text-red-700 rounded-lg">
      <p>Erro ao carregar dados: {{ error }}</p>
    </div>

    <div v-if="!loading && formData" class="max-w-3xl mx-auto bg-white rounded-2xl shadow-lg p-8 border border-gray-200">
      <form @submit.prevent="handleUpdate" class="space-y-8">
        <!-- Dados Pessoais -->
        <section>
          <h2 class="text-xl font-semibold text-gray-900 border-b pb-3 mb-6">Dados Pessoais</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-2">
              <label for="nome" class="block text-sm font-medium text-gray-700">Nome</label>
              <input type="text" id="nome" v-model="formattedNome" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="sobrenome" class="block text-sm font-medium text-gray-700">Sobrenome</label>
              <input type="text" id="sobrenome" v-model="formattedSobrenome" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input type="email" id="email" v-model="formData.email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="telefone" class="block text-sm font-medium text-gray-700">Telefone</label>
              <input type="tel" id="telefone" v-model="formattedTelefone" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2 md:col-span-2">
              <label for="cpf" class="block text-sm font-medium text-gray-700">CPF</label>
              <input type="text" id="cpf" :value="formatCpf(formData.cpf)" disabled class="w-full px-4 py-2 border border-gray-200 bg-gray-100 rounded-lg cursor-not-allowed">
            </div>
            <div class="space-y-2 md:col-span-2">
              <label for="nova_senha" class="block text-sm font-medium text-gray-700">Nova Senha (Opcional)</label>
              <input type="password" id="nova_senha" v-model="formData.nova_senha" placeholder="Deixe em branco para não alterar" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
          </div>
        </section>

        <!-- Endereço -->
        <section>
          <h2 class="text-xl font-semibold text-gray-900 border-b pb-3 mb-6">Endereço Principal</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="space-y-2 md:col-span-2">
              <label for="logradouro" class="block text-sm font-medium text-gray-700">Logradouro</label>
              <input type="text" id="logradouro" v-model="formData.endereco.logradouro" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="cidade" class="block text-sm font-medium text-gray-700">Cidade</label>
              <input type="text" id="cidade" v-model="formData.endereco.cidade" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="bairro" class="block text-sm font-medium text-gray-700">Bairro</label>
              <input type="text" id="bairro" v-model="formData.endereco.bairro" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="complemento" class="block text-sm font-medium text-gray-700">Complemento</label>
              <input type="text" id="complemento" v-model="formData.endereco.complemento" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
            <div class="space-y-2">
              <label for="tag" class="block text-sm font-medium text-gray-700">Tag</label>
              <input type="text" id="tag" v-model="formData.endereco.tag" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500">
            </div>
          </div>
        </section>

        <!-- Mensagens e Botão -->
        <div class="pt-6 border-t">
           <div v-if="updateError" class="mb-4 p-4 bg-red-100 text-red-700 rounded-lg">
            {{ updateError }}
          </div>
          <div v-if="updateSuccess" class="mb-4 p-4 bg-green-100 text-green-700 rounded-lg">
            {{ updateSuccess }}
          </div>
          <div class="flex justify-end space-x-4">
            <RouterLink to="/dashboard/admin/clientes" class="px-6 py-2 text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors">Voltar</RouterLink>
            <button type="submit" :disabled="updateLoading" class="px-6 py-2 font-semibold text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-blue-300 transition-colors">
              <span v-if="updateLoading">Salvando...</span>
              <span v-else>Salvar Alterações</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';
import { useCharacterOnlyFormatter } from '@/composables/useCharacterOnlyFormatter';
import { usePhoneFormatter } from '@/composables/usePhoneFormatter';
import { useCpfFormatter } from '@/composables/useCpfFormatter';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useErrorMessage } from '@/composables/useErrorMessage';

const props = defineProps({
  id: {
    type: String,
    required: true
  }
});

const { successUpdate } = useSuccessMessage();
const { showApiError } = useErrorMessage();

const router = useRouter();
const clienteId = props.id;

const loading = ref(true);
const error = ref(null);
const updateLoading = ref(false);
const updateError = ref(null);
const updateSuccess = ref(null);

const { text: formattedNome } = useCharacterOnlyFormatter();
const { text: formattedSobrenome } = useCharacterOnlyFormatter();
const { phone: formattedTelefone } = usePhoneFormatter();
const { formatCpf } = useCpfFormatter();

const formData = reactive({
  nome: '',
  sobrenome: '',
  cpf: '',
  nova_senha: '',
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
watch(formattedTelefone, (newValue) => { formData.telefone = newValue.replace(/\D/g, ''); });

onMounted(async () => {
  try {
    const response = await api.get(`/clientes/${clienteId}`);
    const cliente = response.data;
    const [nome, ...sobrenomeParts] = cliente.nome.split(' ');
    formattedNome.value = nome;
    formattedSobrenome.value = sobrenomeParts.join(' ');
    formData.cpf = cliente.cpf;

    const emailPrincipal = cliente.contatos.find(c => c.tipo === 'email' && c.tag === 'Principal');
    if (emailPrincipal) formData.email = emailPrincipal.valor;

    const telefonePrincipal = cliente.contatos.find(c => c.tipo === 'telefone' && c.tag === 'Principal');
    if (telefonePrincipal) formattedTelefone.value = telefonePrincipal.valor;

    if (cliente.enderecos && cliente.enderecos.length > 0) {
      const enderecoPrincipal = cliente.enderecos[0];
      formData.endereco = { ...enderecoPrincipal };
    }

  } catch (err) {
    console.error('Erro ao buscar dados do cliente:', err);
    showApiError(err.response?.data?.detail || 'Não foi possível carregar os dados do cliente.');
  } finally {
    loading.value = false;
  }
});

const handleUpdate = async () => {
  updateLoading.value = true;
  updateError.value = null;
  updateSuccess.value = null;

  try {
    const payload = {
      nome: formData.nome,
      sobrenome: formData.sobrenome,
      nova_senha: formData.nova_senha || null,
      email: formData.email,
      telefone: formData.telefone,
      endereco: formData.endereco
    };

    await api.put(`/clientes/admin/${clienteId}`, payload);
    successUpdate('Cliente');
    setTimeout(() => {
      router.push('/dashboard/admin/clientes');
    }, 2000);

  } catch (err) {
    console.error('Erro ao atualizar cliente:', err);
    showApiError(err.response?.data?.detail || 'Ocorreu um erro ao atualizar o cliente.');
  } finally {
    updateLoading.value = false;
  }
};
</script>
