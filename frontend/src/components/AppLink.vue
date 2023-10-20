<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps(RouterLink.props)
const isExternal = computed(() => typeof props.to == 'string' && props.to.startsWith('http'))
</script>

<template>
  <a v-if="isExternal" :href="to"><slot /></a>
  <router-link v-else v-bind="props"><slot /></router-link>
</template>
