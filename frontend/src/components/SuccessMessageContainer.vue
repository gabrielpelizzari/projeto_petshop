<template>
  <div class="fixed top-4 right-4 z-50 space-y-2 pointer-events-none">
    <TransitionGroup
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 translate-x-full"
      enter-to-class="opacity-100 translate-x-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-x-0"
      leave-to-class="opacity-0 translate-x-full"
      move-class="transition-transform duration-300"
    >
      <SuccessMessage
        v-for="message in messages"
        :key="message.id"
        :message="message.message"
        :title="message.title"
        :duration="message.duration"
        :auto-close="message.autoClose"
        @close="removeMessage(message.id)"
        class="pointer-events-auto"
      />
    </TransitionGroup>
  </div>
</template>

<script setup>
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import SuccessMessage from './SuccessMessage.vue';

const { messages, removeMessage } = useSuccessMessage();
</script>
