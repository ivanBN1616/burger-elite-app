<template>
  <div id="app" class="min-h-screen text-green-300">
    <Navbar />
    <HomeView />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import HomeView from './views/HomeView.vue'
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Roboto+Mono&display=swap');

#app { font-family: 'Roboto Mono', monospace; }
</style>
