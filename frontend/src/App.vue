<script setup>
import TheNavbar from '@/components/TheNavbar.vue'
</script>

<template>
  <TheNavbar />
  <main>
    <router-view name="filterBar"></router-view>
    <router-view></router-view>
  </main>
</template>
