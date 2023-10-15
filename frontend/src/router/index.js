import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/nobel-prizes',
      name: 'nobel-prizes',
      component: () => import('@/views/NobelPrizesView.vue')
    },
    {
      path: '/nobel-laureates',
      name: 'nobel-laureates',
      component: () => import('@/views/NobelLaureatesView.vue')
    }
  ]
})

export default router
