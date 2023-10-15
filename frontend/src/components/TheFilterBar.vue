<script setup>
import '@vueform/multiselect/themes/default.css'
import Multiselect from '@vueform/multiselect'
import { useFilterStore } from '@/stores/filterStore'

const filterStore = useFilterStore()
</script>

<template>
  <div class="wrapper">
    <Multiselect
      v-model="filterStore.filter.category"
      :options="filterStore.prizeCategories"
      mode="single"
      placeholder="Filter by prize category"
    />
  </div>
</template>

<style scoped>
.wrapper {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1rem;
}
</style>
