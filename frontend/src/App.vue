<template>
  <div id="app" class="min-h-screen">
    <TheHeader />
    <HomeView />
  </div>
</template>

<script setup>
import TheHeader from './components/TheHeader.vue'
import HomeView from './views/HomeView.vue'
</script>

<style>
#app { 
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
  background-color: #000000;
  color: #ffffff;
}
</style>
