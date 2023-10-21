import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: HomeView
      }
    },
    {
      path: '/nobel-prizes',
      name: 'nobel-prizes',
      components: {
        default: () => import('@/views/NobelPrizesView.vue'),
        filterBar: () => import('@/components/TheFilterBar.vue')
      }
    },
    {
      path: '/nobel-laureates',
      name: 'nobel-laureates',
      components: {
        default: () => import('@/views/NobelLaureatesView.vue'),
        filterBar: () => import('@/components/TheFilterBar.vue')
      }
    }
  ]
})

export default router
