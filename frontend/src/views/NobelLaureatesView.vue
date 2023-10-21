<script setup>
import { useNobelLaureatesStore } from '@/stores/nobelLaureates'

const nobelLaureatesStore = useNobelLaureatesStore()
</script>

<template>
  <EasyDataTable
    v-model:server-options="nobelLaureatesStore.serverOptions"
    :server-items-length="nobelLaureatesStore.totalCount"
    :loading="nobelLaureatesStore.isLoading"
    :headers="nobelLaureatesStore.headers"
    :items="nobelLaureatesStore.nobelLaureates"
    :rows-items="nobelLaureatesStore.rowsPerPageOptions"
    alternating
    buttons-pagination
  />
</template>
