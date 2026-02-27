<template>
  <section class="pt-40 pb-32" style="background: radial-gradient(ellipse at top, rgba(0,255,127,0.03), transparent 50%);">
    <div class="max-w-7xl mx-auto px-8">
      <div class="max-w-3xl">
        <h1 class="text-6xl font-light mb-6 leading-tight" style="letter-spacing: -0.02em;">Infrastructure for Solana Trading</h1>
        <p class="text-xl text-gray-400 mb-10 max-w-2xl font-light leading-relaxed">Enterprise-grade sniping with military-grade security. Powered by Antigravity anomaly detection.</p>
        <div class="flex items-center gap-6 mb-16">
          <button class="glitch-btn">Get Started</button>
          <a href="#docs" class="text-sm text-gray-400 hover:text-white transition-colors duration-300 flex items-center gap-2">
            <span>Documentation</span>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12L10 8L6 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </div>

        <!-- Enterprise stats row -->
        <div class="grid grid-cols-3 gap-6">
          <div class="border-l border-white/10 pl-4">
            <div class="text-xs text-gray-500 uppercase tracking-wider mb-2">Solana TPS</div>
            <div class="text-3xl font-light">2,500</div>
          </div>
          <div class="border-l border-white/10 pl-4">
            <div class="text-xs text-gray-500 uppercase tracking-wider mb-2">Avg Execution</div>
            <div class="text-3xl font-light">120<span class="text-base text-gray-500 ml-1">ms</span></div>
          </div>
          <div class="border-l border-white/10 pl-4">
            <div class="text-xs text-gray-500 uppercase tracking-wider mb-2">Scans Today</div>
            <div class="text-3xl font-light">12,342</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.text-muted { color: rgba(230,255,242,0.7); }
</style>