import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/LogIn.vue';
import Dashboard from './components/DashBoard.vue'; // Рабочая область

const routes = [
  {
    path: '/login',
    component: Login,  // Загружаем только компонент логина
    meta: { requiresAuth: false },
  },
  {
    path: '/dashboard', 
    component: Dashboard,
    meta: { requiresAuth: true }, 
    beforeEnter: (to, from, next) => {
      const token = localStorage.getItem('token');
      if (!token) {
        next('/login'); // Перенаправить на страницу логина, если нет токена
      } else {
        next();  // Разрешить доступ, если токен существует
      }
    },
//    children: [
//      { path: 'sidebar', component: () => import('./components/SideBar.vue') },
//      { path: 'calving', component: () => import('./components/CalVing.vue') },
//    ]
  },
  { path: '/', redirect: '/login' },  // Редирект на login при открытии корневого URL
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!token) {
      next('/login');  // Если токена нет, перенаправляем на логин
    } else {
      next();  // Если токен есть, продолжаем
    }
  } else {
    next();  // Маршруты, не требующие авторизации, продолжаем без проверки
  }
});

export default router;
