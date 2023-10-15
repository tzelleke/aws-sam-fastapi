<script setup>
import { RouterLink } from 'vue-router'

const docsUrl = import.meta.env.BASE_URL + 'docs'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/nobel-prizes">Nobel Prizes</RouterLink>
      <RouterLink to="/nobel-laureates">Nobel Laureates</RouterLink>
      <a :href="docsUrl">API Docs</a>
    </nav>
  </header>
</template>

<style scoped>
nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
