import { ref } from 'vue';

// Estado global das confirmações
const confirmations = ref([]);
let confirmationId = 0;

/**
 * Composable para gerenciar modais de confirmação.
 */
export function useConfirmation() {
  
  /**
   * Exibe um modal de confirmação.
   * 
   * @param {string} message - Mensagem a ser exibida
   * @param {Object} options - Opções do modal
   * @returns {Promise<boolean>} - Promise que resolve com true se confirmado, false se cancelado
   */
  const showConfirmation = (message, options = {}) => {
    return new Promise((resolve) => {
      const id = ++confirmationId;
      const confirmationData = {
        id,
        message,
        title: options.title || 'Confirmação',
        confirmText: options.confirmText || 'Confirmar',
        cancelText: options.cancelText || 'Cancelar',
        variant: options.variant || 'primary',
        resolve
      };
      
      confirmations.value.push(confirmationData);
    });
  };

  /**
   * Confirma exclusão de um item.
   * 
   * @param {string} item - Nome do item a ser excluído
   */
  const confirmDelete = (item = 'este item') => {
    return showConfirmation(
      `Tem certeza que deseja excluir ${item}?`,
      {
        title: 'Confirmar Exclusão',
        confirmText: 'Excluir',
        variant: 'danger'
      }
    );
  };

  /**
   * Confirma logout do sistema.
   */
  const confirmLogout = () => {
    return showConfirmation(
      'Tem certeza que deseja sair do sistema?',
      {
        title: 'Sair do Sistema',
        confirmText: 'Sair'
      }
    );
  };

  /**
   * Confirma descarte de alterações não salvas.
   */
  const confirmDiscardChanges = () => {
    return showConfirmation(
      'Você tem alterações não salvas. Tem certeza que deseja sair sem salvar?',
      {
        title: 'Alterações Não Salvas',
        confirmText: 'Descartar',
        cancelText: 'Continuar Editando',
        variant: 'danger'
      }
    );
  };
  
  /**
   * Remove uma confirmação específica.
   */
  const removeConfirmation = (id) => {
    const index = confirmations.value.findIndex(conf => conf.id === id);
    if (index !== -1) {
      confirmations.value.splice(index, 1);
    }
  };
  
  /**
   * Confirma uma ação específica.
   */
  const confirmAction = (id) => {
    const confirmation = confirmations.value.find(conf => conf.id === id);
    if (confirmation) {
      confirmation.resolve(true);
      removeConfirmation(id);
    }
  };
  
  /**
   * Cancela uma ação específica.
   */
  const cancelAction = (id) => {
    const confirmation = confirmations.value.find(conf => conf.id === id);
    if (confirmation) {
      confirmation.resolve(false);
      removeConfirmation(id);
    }
  };
  
  return {
    confirmations,
    showConfirmation,
    confirmDelete,
    confirmLogout,
    confirmDiscardChanges,
    confirmAction,
    cancelAction,
    removeConfirmation
  };
}
