import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useArrayMap } from '@vueuse/core'
import { useApi } from '@/composables/uesApi'
import { useFilterStore } from '@/stores/filterStore'
import { loadPage } from '@/util/loadPage'

const rowsPerPageOptions = [5, 10, 25]

const headers = [
  { text: 'AWARD YEAR', value: 'award_year' },
  { text: 'CATEGORY', value: 'category' },
  { text: 'LAUREATES', value: 'laureates' }
]

export const useNobelPrizesStore = defineStore('nobelPrizes', () => {
  const serverOptions = ref({
    page: 1,
    rowsPerPage: rowsPerPageOptions[1]
  })
  const filterStore = useFilterStore()
  const { records, isLoading, totalCount, execute } = useApi('nobel-prizes')
  const nobelPrizes = useArrayMap(records, (nobelPrize) => {
    nobelPrize.laureates = (nobelPrize.laureates || []).map((laureate) => laureate.name).join(', ')
    return nobelPrize
  })
  loadPage(serverOptions, filterStore.filter, execute)

  return {
    headers,
    isLoading,
    nobelPrizes,
    rowsPerPageOptions,
    serverOptions,
    totalCount
  }
})
