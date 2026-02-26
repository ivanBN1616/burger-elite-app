<template>
  <header class="flex justify-between items-center p-4 bg-black bg-opacity-40 rounded-lg glass-effect">
    <div class="font-pixel text-xl text-green-300">BURGER ELITE</div>
    <div class="flex space-x-6 text-sm">
      <div>SOL/USD: <span class="text-green-400">$25.67</span></div>
      <div>TPS: <span class="text-green-400">2500</span></div>
      <div>Scanners: <span class="text-green-400">SNIPER, ANTIGRAVITY</span></div>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
.glass-effect { backdrop-filter: blur(8px); border: 1px solid rgba(0,255,0,0.08); }
</style>
