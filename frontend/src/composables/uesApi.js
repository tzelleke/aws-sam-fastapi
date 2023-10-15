import { computed } from 'vue'
import axios from 'axios'
import { useAxios } from '@vueuse/integrations/useAxios'

const baseURL = `${import.meta.env.BASE_URL}api/v1`

export function useApi(endpoint) {
  const instance = axios.create({ baseURL })
  const { data, isLoading, execute } = useAxios(`/${endpoint}`, instance, {
    immediate: false
  })
  const records = computed(() => {
    console.log('useApi', endpoint, data.value)
    return data.value ? data.value.records : []
  })
  const totalCount = computed(() => (data.value ? data.value.meta.count : 0))

  return {
    isLoading,
    records,
    totalCount,
    execute
  }
}
