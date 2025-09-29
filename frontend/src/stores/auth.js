import { defineStore } from 'pinia';
import api from '@/services/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    usuario: JSON.parse(localStorage.getItem('usuario')) || null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
    isAdmin: (state) => state.usuario?.perfil === 'admin',
  },

  actions: {
    async login(cpf, senha) {
      try {
        const params = new URLSearchParams();
        params.append('username', cpf);
        params.append('password', senha);

        const response = await api.post('/login', params, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        });

        const token = response.data.access_token;
        this.token = token;
        localStorage.setItem('token', token);

        // Após o login, busca os dados do usuário
        await this.fetchUsuario();

        return true;
      } catch (error) {
        console.error('Erro no login:', error);
        this.logout();
        return false;
      }
    },

    async fetchUsuario() {
      if (this.token) {
        try {
          // Configura o interceptor dinamicamente para a requisição do usuário
          api.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
          
          const response = await api.get('/usuarios/me');
          this.usuario = response.data;
          localStorage.setItem('usuario', JSON.stringify(response.data));
        } catch (error) {
          console.error('Erro ao buscar usuário:', error);
          this.logout(); // Se o token for inválido, desloga
        }
      }
    },

    logout() {
      this.token = null;
      this.usuario = null;
      localStorage.removeItem('token');
      localStorage.removeItem('usuario');
      delete api.defaults.headers.common['Authorization'];
      // Opcional: redirecionar para a página de login
      // router.push('/login');
    },

    tryAutoLogin() {
      if (this.token) {
        this.fetchUsuario();
      }
    },
  },
});
