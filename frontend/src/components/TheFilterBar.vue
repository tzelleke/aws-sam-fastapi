<script setup>
import '@vueform/multiselect/themes/default.css'
import '@vueform/slider/themes/default.css'
import Multiselect from '@vueform/multiselect'
import Slider from '@vueform/slider'
import { useFilterStore } from '@/stores/filterStore'

const filterStore = useFilterStore()
</script>

<template>
  <div id="wrapper">
    <div id="category-wrapper">
      <Multiselect
        v-model="filterStore.filter.category"
        :options="filterStore.prizeCategories"
        mode="single"
        placeholder="Filter by prize category"
      />
    </div>
    <div id="year-range-wrapper">
      <Slider v-model="filterStore.filter.yearRange" v-bind="filterStore.yearRangeSliderOptions" />
    </div>
  </div>
</template>

<style scoped>
#wrapper {
  display: flex;
  align-items: center;
  width: 100%;
}
#category-wrapper {
  max-width: 18rem;
  flex-grow: 1;
}
#year-range-wrapper {
  flex-grow: 1;
  margin-top: 3rem;
  margin-bottom: 1rem;
  padding: 0 2.5rem;
}
</style>
