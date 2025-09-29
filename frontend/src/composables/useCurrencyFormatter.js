import { ref, watch } from 'vue';

/**
 * Composable para formatar e manipular valores monetários.
 * @param {object} options - Opções de formatação.
 * @param {number} [options.max=1000000] - Valor máximo permitido.
 * @param {string} [options.prefix='R$ '] - Prefixo da moeda.
 */
export function useCurrencyFormatter(options = {}) {
  const { max = 5000000, prefix = 'R$ ' } = options;

  const formattedValue = ref('');
  const numericValue = ref(0);

  const formatCurrency = (value) => {
    if (value === null || value === undefined) return '';

    // Remove tudo que não for dígito
    let digits = String(value).replace(/\D/g, '');
    if (digits === '') return '';

    let number = parseInt(digits, 10) / 100;

    // Aplica o limite máximo
    if (number > max) {
      number = max;
      digits = String(max * 100);
    }

    numericValue.value = number;

    // Formata para o padrão BRL
    const formatted = new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL',
      minimumFractionDigits: 2
    }).format(number);

    return formatted;
  };

  watch(formattedValue, (newVal, oldVal) => {
    // Evita loop infinito e permite apagar o campo
    if (newVal === '' && oldVal !== '') {
        numericValue.value = 0;
        return;
    }

    const newFormatted = formatCurrency(newVal);
    if (newFormatted !== formattedValue.value) {
      formattedValue.value = newFormatted;
    }
  });

  const setValue = (number) => {
    if (typeof number !== 'number') return;
    const val = number.toFixed(2).replace('.', '');
    formattedValue.value = formatCurrency(val);
  };

  return {
    formattedValue,
    numericValue,
    setValue
  };
}
