<template>
  <div id="app" class="min-h-screen">
    <Navbar />
    <HomeView />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import HomeView from './views/HomeView.vue'
</script>

<style>
#app { 
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
  background-color: #020202;
  color: #e0e0e0;
}
</style>
