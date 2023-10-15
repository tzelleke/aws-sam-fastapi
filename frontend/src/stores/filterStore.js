import { ref } from 'vue'
import { defineStore } from 'pinia'

const prizeCategories = [
  { value: 'che', label: 'Chemistry' },
  { value: 'eco', label: 'Economic Sciences' },
  { value: 'lit', label: 'Literature' },
  { value: 'pea', label: 'Peace' },
  { value: 'phy', label: 'Physics' },
  { value: 'med', label: 'Physiology or Medicine' }
]

export const useFilterStore = defineStore('filter', () => {
  const filter = ref({
    category: null,
    search: ''
  })

  return {
    filter,
    prizeCategories
  }
})
