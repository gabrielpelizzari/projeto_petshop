<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-green-50">
    <!-- Header/Navigation -->
    <header class="relative z-10 bg-white/80 backdrop-blur-md border-b border-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <div class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-gradient-to-br from-blue-500 to-green-500 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
                <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
              </svg>
            </div>
            <span class="text-xl font-bold bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">
              PetHub
            </span>
          </div>

          <!-- Action Buttons -->
          <div class="flex items-center space-x-3">
            <RouterLink 
              to="/login"
              class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200"
            >
              Entrar
            </RouterLink>
            <RouterLink 
              to="/cadastro"
              class="px-6 py-2 bg-gradient-to-r from-blue-600 to-green-600 text-white text-sm font-medium rounded-lg hover:from-blue-700 hover:to-green-700 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
            >
              Cadastrar
            </RouterLink>
          </div>
        </div>
      </div>
    </header>

    <!-- Hero Section -->
    <main class="relative">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16">
        <div class="text-center">
          <!-- Main Heading -->
          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 mb-6">
            Cuidado completo para
            <span class="bg-gradient-to-r from-blue-600 to-green-600 bg-clip-text text-transparent">
              seu melhor amigo
            </span>
          </h1>
          
          <!-- Subtitle -->
          <p class="text-xl text-gray-600 mb-12 max-w-3xl mx-auto leading-relaxed">
            Oferecemos serviços veterinários de qualidade, com profissionais especializados 
            e tecnologia moderna para garantir a saúde e bem-estar do seu pet.
          </p>

          <!-- CTA Buttons -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-16">
            <RouterLink 
              to="/cadastro"
              class="w-full sm:w-auto px-8 py-4 bg-gradient-to-r from-blue-600 to-green-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-green-700 transform hover:scale-105 transition-all duration-200 shadow-xl hover:shadow-2xl"
            >
              Começar Agora
            </RouterLink>
            <RouterLink 
              to="/login"
              class="w-full sm:w-auto px-8 py-4 bg-white text-gray-700 font-semibold rounded-xl border-2 border-gray-200 hover:border-gray-300 hover:bg-gray-50 transition-all duration-200"
            >
              Já tenho conta
            </RouterLink>
          </div>

          <!-- Features Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-20">
            <!-- Feature 1 -->
            <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-8 border border-gray-100 hover:shadow-lg transition-all duration-300">
              <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center mb-4 mx-auto">
                <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-3">Consultas Especializadas</h3>
              <p class="text-gray-600 leading-relaxed">
                Veterinários experientes para Cuidar da saúde do seu pet com excelência e carinho.
              </p>
            </div>

            <!-- Feature 2 -->
            <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-8 border border-gray-100 hover:shadow-lg transition-all duration-300">
              <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center mb-4 mx-auto">
                <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-3">Agendamento Fácil</h3>
              <p class="text-gray-600 leading-relaxed">
                Sistema online intuitivo para agendar consultas e acompanhar o histórico do seu pet.
              </p>
            </div>

            <!-- Feature 3 -->
            <div class="bg-white/60 backdrop-blur-sm rounded-2xl p-8 border border-gray-100 hover:shadow-lg transition-all duration-300">
              <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center mb-4 mx-auto">
                <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold text-gray-900 mb-3">Cuidado Personalizado</h3>
              <p class="text-gray-600 leading-relaxed">
                Atendimento individualizado respeitando as necessidades específicas de cada animal.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Decorative Elements -->
      <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div class="absolute top-20 left-10 w-20 h-20 bg-blue-200/30 rounded-full blur-xl"></div>
        <div class="absolute top-40 right-20 w-32 h-32 bg-green-200/30 rounded-full blur-xl"></div>
        <div class="absolute bottom-20 left-1/4 w-24 h-24 bg-purple-200/30 rounded-full blur-xl"></div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white/80 backdrop-blur-md border-t border-gray-100 mt-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="text-center text-gray-600">
          <p>&copy; 2024 PetHub. Todos os direitos reservados.</p>
          <p class="mt-2 text-sm">Cuidando do seu pet com amor e profissionalismo.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>