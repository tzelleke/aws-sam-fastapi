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

const yearRangeSliderOptions = {
  min: 1901,
  max: 2023,
  merge: 10
}

export const useFilterStore = defineStore('filter', () => {
  const filter = ref({
    category: null,
    yearRange: [1901, 2023]
  })

  return {
    filter,
    prizeCategories,
    yearRangeSliderOptions
  }
})
