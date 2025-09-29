<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-50">
    <!-- Decorative Elements -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-20 h-20 bg-blue-200/20 rounded-full blur-xl"></div>
      <div class="absolute top-40 right-20 w-32 h-32 bg-green-200/20 rounded-full blur-xl"></div>
      <div class="absolute bottom-20 left-1/4 w-24 h-24 bg-purple-200/20 rounded-full blur-xl"></div>
    </div>

    <div class="flex h-screen relative">
      <!-- Sidebar -->
      <aside class="w-72 bg-white/70 backdrop-blur-md border-r border-gray-200/50 flex flex-col shadow-xl">
        <!-- Header com Logo -->
        <div class="p-6 border-b border-gray-200/50">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-green-500 rounded-xl flex items-center justify-center">
              <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
                <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
              </svg>
            </div>
            <div>
              <h1 class="text-xl font-bold bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">
                PetHub
              </h1>
              <p class="text-sm text-gray-500">Painel Administrativo</p>
            </div>
          </div>
        </div>

        <!-- Navigation -->
        <nav class="flex-1 p-6 space-y-2">
          <div class="mb-6">
            <h3 class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3">
              Navegação Principal
            </h3>
            
            <!-- Dashboard Overview -->
            <RouterLink
              to="/dashboard/admin"
              class="group flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all duration-200 hover:bg-white/60 hover:shadow-sm"
              active-class="bg-gradient-to-r from-blue-500/10 to-green-500/10 text-blue-700 shadow-sm"
              exact-active-class="bg-gradient-to-r from-blue-500/10 to-green-500/10 text-blue-700 shadow-sm"
            >
              <svg class="w-5 h-5 mr-3 text-gray-400 group-hover:text-blue-500 transition-colors duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2-2z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5a2 2 0 012-2h4a2 2 0 012 2v6H8V5z"/>
              </svg>
              <span class="group-hover:text-gray-900 transition-colors duration-200">Dashboard</span>
            </RouterLink>

                        <!-- Atendimentos -->
            <RouterLink
              to="/dashboard/admin/atendimentos"
              class="group flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all duration-200 hover:bg-white/60 hover:shadow-sm"
              active-class="bg-gradient-to-r from-blue-500/10 to-green-500/10 text-blue-700 shadow-sm"
            >
              <svg class="w-5 h-5 mr-3 text-gray-400 group-hover:text-purple-500 transition-colors duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/>
              </svg>
              <span class="group-hover:text-gray-900 transition-colors duration-200">Atendimentos</span>
            </RouterLink>

            <!-- Clientes -->
            <RouterLink
              to="/dashboard/admin/clientes"
              class="group flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all duration-200 hover:bg-white/60 hover:shadow-sm"
              active-class="bg-gradient-to-r from-blue-500/10 to-green-500/10 text-blue-700 shadow-sm"
            >
              <svg class="w-5 h-5 mr-3 text-gray-400 group-hover:text-blue-500 transition-colors duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z"/>
              </svg>
              <span class="group-hover:text-gray-900 transition-colors duration-200">Clientes</span>
            </RouterLink>

            <!-- Pets -->
            <RouterLink
              to="/dashboard/admin/pets"
              class="group flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all duration-200 hover:bg-white/60 hover:shadow-sm"
              active-class="bg-gradient-to-r from-blue-500/10 to-green-500/10 text-blue-700 shadow-sm"
            >
              <svg class="w-5 h-5 mr-3 text-gray-400 group-hover:text-green-500 transition-colors duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
              <span class="group-hover:text-gray-900 transition-colors duration-200">Pets</span>
            </RouterLink>

            <!-- Raças -->
            <RouterLink
              to="/dashboard/admin/racas"
              class="group flex items-center px-4 py-3 text-sm font-medium rounded-xl transition-all duration-200 hover:bg-white/60 hover:shadow-sm"
              active-class="bg-gradient-to-r from-blue-500/10 to-green-500/10 text-blue-700 shadow-sm"
            >
              <svg class="w-5 h-5 mr-3 text-gray-400 group-hover:text-orange-500 transition-colors duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14-7H3a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2z"/>
              </svg>
              <span class="group-hover:text-gray-900 transition-colors duration-200">Raças</span>
            </RouterLink>


          </div>
        </nav>

        <!-- Footer da Sidebar -->
        <div class="p-6 border-t border-gray-200/50">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-gradient-to-br from-gray-400 to-gray-600 rounded-lg flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
              <div>
                <p class="text-sm font-medium text-gray-700">Administrador</p>
                <p class="text-xs text-gray-500">Online</p>
              </div>
            </div>
            <button
              @click="handleLogout"
              class="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
              title="Sair"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
              </svg>
            </button>
          </div>
        </div>
      </aside>

      <!-- Main Content Area -->
      <main class="flex-1 overflow-y-auto">
        <div class="p-8">
          <RouterView />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useSuccessMessage } from '@/composables/useSuccessMessage';
import { useConfirmation } from '@/composables/useConfirmationMessage';

const { showSuccess } = useSuccessMessage();
const { confirmLogout } = useConfirmation();
const router = useRouter();
const authStore = useAuthStore();

const handleLogout = async () => {
  const confirmed = await confirmLogout();
  
  if (confirmed) {
    authStore.logout();
    router.push('/home');
    showSuccess('Sessão encerrada com sucesso!');
  }
};
</script>
