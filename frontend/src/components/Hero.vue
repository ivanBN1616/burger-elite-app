<template>
  <section class="pt-48 pb-40">
    <div class="max-w-7xl mx-auto px-8 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
      <!-- Left Column: Text Content -->
      <div class="max-w-xl">
        <h2 class="text-sm text-gray-500 uppercase tracking-widest mb-8">We Make</h2>
        <h1 class="text-8xl font-light mb-8 leading-none" style="letter-spacing: -0.03em;">Solana Sniping<br/>Simple</h1>
        <p class="text-2xl text-gray-400 mb-16 max-w-3xl font-light leading-relaxed">The most trusted anti-rugpull infrastructure for Solana trading</p>
        <div class="flex items-center gap-6">
          <button class="glitch-btn text-base">Get Started</button>
          <a href="#docs" class="text-base text-gray-400 hover:text-white transition-colors duration-300">
            Documentation
          </a>
        </div>
      </div>

      <!-- Right Column: NFT with Glass Frame -->
      <div class="flex justify-center lg:justify-end">
        <div class="w-96 h-96 rounded-lg border border-white/10 glass-effect flex items-center justify-center p-8">
          <img src="/assets/placeholder-nft.svg" alt="Burger Sniper NFT" class="max-w-full h-auto object-contain"/>
          <!-- TODO: Replace with optimized Burger Sniper NFT asset -->
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