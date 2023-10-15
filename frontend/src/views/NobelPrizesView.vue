<script setup>
import { useNobelPrizesStore } from '@/stores/nobelPrizes'
import TheFilterBar from '@/components/TheFilterBar.vue'

const nobelPrizesStore = useNobelPrizesStore()
</script>

<template>
  <TheFilterBar />
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
