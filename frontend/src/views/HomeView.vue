<script setup>
import logoUrl from '@/assets/logo.svg'
import HelloWorld from '@/components/HelloWorld.vue'
import TheWelcome from '@/components/TheWelcome.vue'
</script>

<template>
  <div id="grid">
    <div class="outer">
      <img alt="Vue logo" class="logo" :src="logoUrl" width="125" height="125" />

      <div class="inner">
        <HelloWorld msg="You did it!" />
      </div>
    </div>

    <div>
      <TheWelcome />
    </div>
  </div>
</template>

<style scoped>
div.outer {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  div.outer {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  div.outer .inner {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

@media (min-width: 1024px) {
  #grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }
}
</style>
