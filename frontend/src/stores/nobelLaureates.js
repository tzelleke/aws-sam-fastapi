import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useArrayMap } from '@vueuse/core'
import { useApi } from '@/composables/uesApi'
import { useFilterStore } from '@/stores/filterStore'
import { loadPage } from '@/util/loadPage'

const rowsPerPageOptions = [5, 10, 25]

const headers = [
  { text: 'NAME', value: 'name' },
  { text: 'GENDER', value: 'gender' },
  { text: 'BIRTH DATE', value: 'birth_date' },
  { text: 'DEATH DATE', value: 'death_date' },
  { text: 'NOBEL PRIZES', value: 'prizes' },
  { text: 'BIRTH COUNTRY', value: 'birth_country' }
]

export const useNobelLaureatesStore = defineStore('nobelLaureates', () => {
  const serverOptions = ref({
    page: 1,
    rowsPerPage: rowsPerPageOptions[1]
  })
  const filterStore = useFilterStore()
  const { records, isLoading, totalCount, execute } = useApi('nobel-laureates')
  const nobelLaureates = useArrayMap(records, (laureate) => {
    laureate.prizes = laureate.prizes
      .map((prize) => `${prize.award_year} ${prize.category}`)
      .join(', ')
    return laureate
  })
  loadPage(serverOptions, filterStore.filter, execute)

  return {
    headers,
    isLoading,
    nobelLaureates,
    rowsPerPageOptions,
    serverOptions,
    totalCount
  }
})
