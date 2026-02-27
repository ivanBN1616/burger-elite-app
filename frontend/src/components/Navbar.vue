<template>
  <nav class="fixed top-0 left-0 right-0 z-50 border-b border-white/10" style="backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); background: rgba(2,2,2,0.8);">
    <div class="max-w-7xl mx-auto flex items-center justify-between px-8 py-4">
      <div class="text-base font-light tracking-wide">BURGER ELITE</div>
      <div class="flex items-center space-x-8">
        <div class="relative group">
          <button class="text-sm text-gray-400 hover:text-white transition-colors duration-300">Products</button>
          <div class="absolute right-0 mt-3 w-72 bg-black/90 border border-white/10 rounded-lg shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 p-6" style="backdrop-filter: blur(24px);">
            <div class="mb-4">
              <div class="text-sm font-normal mb-1">Sniper Engine</div>
              <div class="text-xs text-gray-500">Fast execution layer</div>
            </div>
            <div class="mb-4 pt-4 border-t border-white/10">
              <div class="text-sm font-normal mb-1">Antigravity Core</div>
              <div class="text-xs text-gray-500">Security and anomaly detection</div>
            </div>
            <div class="pt-4 border-t border-white/10">
              <div class="text-sm font-normal mb-1">API / Docs</div>
              <div class="text-xs text-gray-500">Integrate via websocket & REST</div>
            </div>
          </div>
        </div>
        <a href="#features" class="text-sm text-gray-400 hover:text-white transition-colors duration-300">Features</a>
        <a href="#tiers" class="text-sm text-gray-400 hover:text-white transition-colors duration-300">Solutions</a>
        <a href="#docs" class="text-sm text-gray-400 hover:text-white transition-colors duration-300">Docs</a>
        <button class="text-sm px-6 py-2 rounded-md border border-white/20 hover:bg-white/5 transition-all duration-300">Sign In</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
</script>

<style scoped>
</style>