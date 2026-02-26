<template>
  <section class="pt-28 pb-12">
    <div class="max-w-6xl mx-auto">
      <div class="grid md:grid-cols-2 gap-8 items-center">
        <div>
          <h1 class="text-4xl md:text-5xl font-semibold mb-4">DOMINA SOLANA CON BURGER ELITE</h1>
          <p class="text-muted mb-6 max-w-lg">Sniping a velocidad de la luz. Seguridad de grado industrial impulsada por Antigravity.</p>
          <div class="flex items-center gap-4">
            <button class="glitch-btn px-8 py-3">Get Started</button>
            <a href="#docs" class="text-sm text-muted hover:text-green-300">Docs & API</a>
          </div>

          <!-- compact stats row like Photon -->
          <div class="mt-8 grid grid-cols-3 gap-3">
            <div class="card p-3 text-center">
              <div class="text-xs text-muted">Solana TPS</div>
              <div class="text-lg font-bold text-green-300">2,500</div>
            </div>
            <div class="card p-3 text-center">
              <div class="text-xs text-muted">Avg Exec</div>
              <div class="text-lg font-bold text-green-300">120 ms</div>
            </div>
            <div class="card p-3 text-center">
              <div class="text-xs text-muted">Today Scans</div>
              <div class="text-lg font-bold text-fuchsia-400">12,342</div>
            </div>
          </div>
        </div>
        <div class="flex justify-center">
          <div class="w-96">
            <img src="/assets/placeholder-nft.svg" alt="Burger Sniper NFT" class="w-full rounded-lg shadow-2xl">
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.glitch-btn { background: linear-gradient(90deg,#00ff7f,#a100ff); color:#020202; border-radius:12px; }
.font-pixel { font-family: 'Press Start 2P', cursive; }
</style>