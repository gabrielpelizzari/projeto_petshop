import { ref, watch } from 'vue';

export function usePhoneFormatter(initialValue = '') {
  const phone = ref(initialValue);

  const formatPhone = (value) => {
    if (!value) return '';

    let digitsOnly = value.toString().replace(/\D/g, '');

    if (digitsOnly.length > 11) {
      digitsOnly = digitsOnly.slice(0, 11);
    }

    if (digitsOnly.length > 10) {
      // (XX) XXXXX-XXXX
      return `(${digitsOnly.slice(0, 2)}) ${digitsOnly.slice(2, 7)}-${digitsOnly.slice(7)}`;
    } else if (digitsOnly.length > 6) {
      // (XX) XXXX-XXXX
      return `(${digitsOnly.slice(0, 2)}) ${digitsOnly.slice(2, 6)}-${digitsOnly.slice(6)}`;
    } else if (digitsOnly.length > 2) {
      // (XX) XXXX
      return `(${digitsOnly.slice(0, 2)}) ${digitsOnly.slice(2)}`;
    } else if (digitsOnly.length > 0) {
      // (XX
      return `(${digitsOnly}`;
    }

    return digitsOnly;
  };

  watch(phone, (newValue) => {
    const formatted = formatPhone(newValue);
    if (formatted !== newValue) {
      phone.value = formatted;
    }
  });

  return {
    phone,
    formatPhone
  };
}
