import { ref, watch } from 'vue';

export function useCpfFormatter(initialValue = '') {
  const cpf = ref(initialValue);

  const formatCpf = (value) => {
    if (!value) return '';

    // Remove tudo que não for dígito
    let digitsOnly = value.toString().replace(/\D/g, '');

    // Limita a 11 dígitos
    if (digitsOnly.length > 11) {
      digitsOnly = digitsOnly.slice(0, 11);
    }

    // Aplica a máscara
    if (digitsOnly.length > 9) {
      return `${digitsOnly.slice(0, 3)}.${digitsOnly.slice(3, 6)}.${digitsOnly.slice(6, 9)}-${digitsOnly.slice(9)}`;
    } else if (digitsOnly.length > 6) {
      return `${digitsOnly.slice(0, 3)}.${digitsOnly.slice(3, 6)}.${digitsOnly.slice(6)}`;
    } else if (digitsOnly.length > 3) {
      return `${digitsOnly.slice(0, 3)}.${digitsOnly.slice(3)}`;
    }

    return digitsOnly;
  };

  watch(cpf, (newValue, oldValue) => {
    const formatted = formatCpf(newValue);
    if (formatted !== newValue) {
      cpf.value = formatted;
    }
  });

  // Retorna o ref para ser usado com v-model e a função para uso manual se necessário
  return {
    cpf,
    formatCpf
  };
}
