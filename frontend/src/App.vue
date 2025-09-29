<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import SuccessMessageContainer from '@/components/SuccessMessageContainer.vue';
import ErrorMessageContainer from '@/components/ErrorMessageContainer.vue';
import ConfirmationContainer from '@/components/ConfirmationContainer.vue';

const authStore = useAuthStore();

onMounted(() => {
  authStore.tryAutoLogin();
});
</script>

<template>
  <RouterView />
  <SuccessMessageContainer />
  <ErrorMessageContainer />
  <ConfirmationContainer />
</template>