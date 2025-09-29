import { ref } from 'vue';

// Estado global das mensagens de erro
const errorMessages = ref([]);
let errorMessageId = 0;

/**
 * Composable para gerenciar mensagens de erro.
 */
export function useErrorMessage() {
  
  /**
   * Exibe uma mensagem de erro.
   * 
   * @param {string} message - Mensagem a ser exibida
   * @param {Object} options - Opções da mensagem
   */
  const showError = (message, options = {}) => {
    const id = ++errorMessageId;
    const messageData = {
      id,
      message,
      title: options.title || 'Erro!',
      duration: options.duration || 5000,
      autoClose: options.autoClose !== false
    };
    
    errorMessages.value.push(messageData);
    
    // Remove mensagens antigas se houver muitas
    if (errorMessages.value.length > 3) {
      errorMessages.value.shift();
    }
    
    return id;
  };

  /**
   * Processa erro de API e extrai mensagem apropriada.
   */
  const processApiError = (error, fallbackMessage = 'Ocorreu um erro inesperado') => {
    let message = fallbackMessage;
    
    if (error.response?.data?.detail) {
      message = error.response.data.detail;
    } else if (error.response?.data?.message) {
      message = error.response.data.message;
    } else if (error.message) {
      message = error.message;
    }
    
    return message;
  };

  /**
   * Exibe erro de API com processamento automático.
   */
  const showApiError = (error, fallbackMessage) => {
    const message = processApiError(error, fallbackMessage);
    return showError(message);
  };

  /**
   * Helpers para validações comuns.
   */
  const showValidationError = (field) => {
    return showError(`O campo "${field}" é obrigatório.`, { title: 'Campo Obrigatório' });
  };

  const showPasswordMismatch = () => {
    return showError('As senhas não coincidem. Verifique e tente novamente.', { title: 'Senha Inválida' });
  };
  
  /**
   * Remove uma mensagem específica.
   */
  const removeErrorMessage = (id) => {
    const index = errorMessages.value.findIndex(msg => msg.id === id);
    if (index !== -1) {
      errorMessages.value.splice(index, 1);
    }
  };
  
  /**
   * Remove todas as mensagens de erro.
   */
  const clearAllErrors = () => {
    errorMessages.value = [];
  };
  
  return {
    errorMessages,
    showError,
    showApiError,
    showValidationError,
    showPasswordMismatch,
    removeErrorMessage,
    clearAllErrors,
    processApiError
  };
}
