<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-black bg-opacity-60 backdrop-blur-md">
    <div class="max-w-6xl mx-auto flex items-center justify-between p-4">
      <div class="font-pixel text-green-300">BURGER ELITE</div>
      <div class="flex items-center space-x-4">
        <div class="relative group">
          <button class="text-sm">Products</button>
          <div class="absolute right-0 mt-2 w-64 bg-black bg-opacity-70 border border-white/5 rounded shadow-lg opacity-0 group-hover:opacity-100 transition-opacity p-4">
            <div class="text-sm font-bold">Sniper Engine</div>
            <div class="text-xs text-muted">Fast execution layer</div>
            <hr class="my-2 border-white/5" />
            <div class="text-sm font-bold">Antigravity Core</div>
            <div class="text-xs text-muted">Security and anomaly detection</div>
            <hr class="my-2 border-white/5" />
            <div class="text-sm font-bold">API / Docs</div>
            <div class="text-xs text-muted">Integrate via websocket & REST</div>
          </div>
        </div>
        <a href="#features" class="text-sm hover:text-green-400">Features</a>
        <a href="#tiers" class="text-sm hover:text-fuchsia-400">Solutions</a>
        <a href="#docs" class="text-sm hover:text-green-400">Docs</a>
        <a href="#demo" class="text-sm hover:text-fuchsia-400">Demo</a>
      </div>
    </div>
  </nav>
</template>

<script setup>
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
</style>