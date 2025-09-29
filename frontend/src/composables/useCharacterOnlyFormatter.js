import { ref, watch } from 'vue';

/**
 * Formata um valor de input para aceitar apenas caracteres não numéricos.
 * @param {import('vue').Ref<string> | string} initialValue - O valor inicial.
 * @returns {{text: import('vue').Ref<string>, formatText: (value: string) => string}}
 */
export function useCharacterOnlyFormatter(initialValue = '') {
  const text = ref(initialValue);

  const formatText = (value) => {
    if (typeof value !== 'string') {
      return '';
    }
    // Remove todos os dígitos (números)
    return value.replace(/\d/g, '');
  };

  watch(text, (newValue) => {
    const formatted = formatText(newValue);
    if (formatted !== newValue) {
      text.value = formatted;
    }
  });

  // Garante que o valor inicial também seja formatado
  text.value = formatText(text.value);

  return {
    text,
    formatText,
  };
}
