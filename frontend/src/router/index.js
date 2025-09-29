import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import CadastroView from '../views/CadastroView.vue';
import DashboardCliente from '../views/cliente/dashboard/DashboardCliente.vue';
import AdminLayout from '../views/admin/AdminLayout.vue';
import AdminOverview from '../views/admin/dashboard/AdminOverview.vue';
import ClienteList from '../views/admin/clientes/ClienteList.vue';
import ClienteCreate from '../views/admin/clientes/ClienteCreate.vue';
import ClienteEdit from '../views/admin/clientes/ClienteEdit.vue';
import ClienteDetail from '../views/admin/clientes/ClienteDetail.vue';
import PetList from '../views/admin/pets/PetList.vue';
import RacaList from '../views/admin/racas/RacaList.vue';
import AtendimentosAdmin from '../views/admin/atendimentos/AtendimentosAdmin.vue';

const routes = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/cadastro',
    name: 'cadastro',
    component: CadastroView,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    redirect: () => {
      return '/dashboard/cliente'; 
    },
    meta: { requiresAuth: true },
  },
  {
    path: '/dashboard/cliente',
    name: 'dashboard-cliente',
    component: DashboardCliente,
    meta: { requiresAuth: true, isClient: true },
  },
    {
      path: '/dashboard/admin',
      component: AdminLayout,
      meta: { requiresAuth: true, isAdmin: true },
      children: [
        {
          path: '',
          name: 'admin-overview',
          component: AdminOverview,
        },
        {
          path: 'clientes',
          name: 'admin-clientes',
          component: ClienteList,
        },
        {
          path: 'clientes/novo',
          name: 'admin-cliente-novo',
          component: ClienteCreate,
        },
        {
          path: 'clientes/:id/edit',
          name: 'admin-cliente-edit',
          component: ClienteEdit,
          props: true
        },
        {
          path: 'clientes/:id/view',
          name: 'admin-cliente-view',
          component: ClienteDetail,
          props: true
        },
        {
          path: 'pets',
          name: 'admin-pets',
          component: PetList,
        },
        {
          path: 'racas',
          name: 'admin-racas',
          component: RacaList,
        },
        {
          path: 'atendimentos',
          name: 'admin-atendimentos',
          component: AtendimentosAdmin,
        },
      ],
    },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresAdmin = to.matched.some(record => record.meta.isAdmin);
  const requiresClient = to.matched.some(record => record.meta.isClient);

  // Verifica se precisa estar autenticado
  if (requiresAuth && !authStore.isAuthenticated) {
    next('/login');
    return;
  }

  // Verifica se precisa ser admin
  if (requiresAdmin && !authStore.isAdmin) {
    // Redireciona cliente para seu dashboard se tentar acessar área admin
    next({ name: 'dashboard-cliente' });
    return;
  }

  // Verifica se precisa ser cliente
  if (requiresClient && authStore.isAdmin) {
    // Redireciona admin para seu dashboard se tentar acessar área cliente
    next({ name: 'admin-overview' });
    return;
  }

  // Redireciona usuário logado tentando acessar login
  if (to.path === '/login' && authStore.isAuthenticated) {
    next({ name: 'dashboard' });
    return;
  }
  // Lógica de redirecionamento para o dashboard correto
  if (to.name === 'dashboard') {
    if (authStore.isAdmin) {
      next({ name: 'admin-overview' });
    } else {
      next({ name: 'dashboard-cliente' });
    }
    return;
  }

  next();
});

export default router
