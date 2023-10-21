<script setup>
import { useNobelPrizesStore } from '@/stores/nobelPrizes'

const nobelPrizesStore = useNobelPrizesStore()
</script>

<template>
  <EasyDataTable
    v-model:server-options="nobelPrizesStore.serverOptions"
    :server-items-length="nobelPrizesStore.totalCount"
    :loading="nobelPrizesStore.isLoading"
    :headers="nobelPrizesStore.headers"
    :items="nobelPrizesStore.nobelPrizes"
    :rows-items="nobelPrizesStore.rowsPerPageOptions"
    alternating
    buttons-pagination
  />
</template>
