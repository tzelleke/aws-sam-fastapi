import { watch } from 'vue'

export function loadPage(serverOptions, filter, execute) {
  const load = () => {
    const { page, rowsPerPage } = serverOptions.value
    const params = {
      offset: (page - 1) * rowsPerPage,
      limit: rowsPerPage
    }
    if (filter.category) {
      params['nobel-prize-category'] = filter.category
    }
    if (filter.yearRange) {
      params['nobel-prize-year'] = filter.yearRange[0]
      params['nobel-prize-year-to'] = filter.yearRange[1]
    }
    console.log('Loading Page with params:', params)
    execute({ params })
  }

  watch([serverOptions, filter], load, { immediate: true, deep: true })
}
