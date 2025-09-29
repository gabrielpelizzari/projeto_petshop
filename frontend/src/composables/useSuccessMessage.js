import { ref } from 'vue';

// Estado global das mensagens
const messages = ref([]);
let messageId = 0;

/**
 * Composable para gerenciar mensagens de sucesso.
 */
export function useSuccessMessage() {
  
  /**
   * Exibe uma mensagem de sucesso.
   * 
   * @param {string} message - Mensagem a ser exibida
   * @param {Object} options - Opções da mensagem
   */
  const showSuccess = (message, options = {}) => {
    const id = ++messageId;
    const messageData = {
      id,
      message,
      title: options.title || 'Sucesso!',
      duration: options.duration || 4000,
      autoClose: options.autoClose !== false
    };
    
    messages.value.push(messageData);
    
    // Remove mensagens antigas se houver muitas
    if (messages.value.length > 3) {
      messages.value.shift();
    }
    
    return id;
  };

  /**
   * Helpers para operações comuns.
   */
  const successCreate = (item) => showSuccess(`${item} criado com sucesso!`);
  const successUpdate = (item) => showSuccess(`${item} atualizado com sucesso!`);
  const successDelete = (item) => showSuccess(`${item} excluído com sucesso!`);
  const successSave = () => showSuccess('Dados salvos com sucesso!');
  
  /**
   * Remove uma mensagem específica.
   */
  const removeMessage = (id) => {
    const index = messages.value.findIndex(msg => msg.id === id);
    if (index !== -1) {
      messages.value.splice(index, 1);
    }
  };
  
  /**
   * Remove todas as mensagens.
   */
  const clearAll = () => {
    messages.value = [];
  };
  
  return {
    messages,
    showSuccess,
    successCreate,
    successUpdate,
    successDelete,
    successSave,
    removeMessage,
    clearAll
  };
}
