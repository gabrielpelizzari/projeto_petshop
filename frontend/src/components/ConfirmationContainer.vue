<template>
  <div>
    <ConfirmationModal
      v-for="confirmation in confirmations"
      :key="confirmation.id"
      :message="confirmation.message"
      :title="confirmation.title"
      :confirm-text="confirmation.confirmText"
      :cancel-text="confirmation.cancelText"
      :variant="confirmation.variant"
      @confirm="confirmAction(confirmation.id)"
      @cancel="cancelAction(confirmation.id)"
    />
  </div>
</template>

<script setup>
import { useConfirmation } from '@/composables/useConfirmationMessage';
import ConfirmationModal from './ConfirmationModal.vue';

const { confirmations, confirmAction, cancelAction } = useConfirmation();
</script>
