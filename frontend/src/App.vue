<script setup>
import { RouterView } from 'vue-router'
import TheNavbar from '@/components/TheNavbar.vue'
</script>

<template>
  <TheNavbar />
  <main>
    <RouterView />
  </main>
</template>
