<template>
  <header class="fixed top-0 left-0 right-0 z-50 border-b border-white/5" style="backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); background: rgba(2,2,2,0.8);">
    <div class="max-w-7xl mx-auto px-8 py-4 flex items-center justify-between">
      <!-- Left: Logo + Network Status -->
      <div class="flex items-center gap-6">
        <div class="font-mono text-sm tracking-wider text-brand-green">BURGER ELITE</div>
        <div class="flex items-center gap-2 text-xs">
          <div class="w-2 h-2 rounded-full bg-brand-green pulse-green"></div>
          <span class="text-gray-400 font-mono uppercase">NETWORK: <span class="text-brand-green">ONLINE</span></span>
        </div>
      </div>

      <!-- Right: Live SOL Price -->
      <div class="flex items-center gap-6">
        <div class="flex items-center gap-3">
          <div class="text-xs text-gray-500 font-mono uppercase">SOL/USD</div>
          <div class="text-lg font-mono" :class="priceChangeClass">
            {{ solPrice ? `$${solPrice}` : 'Loading...' }}
          </div>
          <div v-if="priceChange" class="text-xs font-mono" :class="priceChangeClass">
            {{ priceChange > 0 ? '+' : '' }}{{ priceChange.toFixed(2) }}%
          </div>
        </div>
        <div class="w-px h-6 bg-white/10"></div>
        <button class="text-xs px-4 py-2 rounded-md border border-white/20 hover:bg-white/5 transition-all duration-300 font-mono">
          CONNECT
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'

const solPrice = ref(null)
const priceChange = ref(null)
let priceInterval = null

const priceChangeClass = computed(() => {
  if (!priceChange.value) return 'text-white'
  return priceChange.value > 0 ? 'text-brand-green' : 'text-red-400'
})

async function fetchSOLPrice() {
  try {
    // Using CoinGecko API (no auth required, 50 calls/min free tier)
    const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true')
    const data = await response.json()
    
    if (data.solana) {
      solPrice.value = data.solana.usd.toFixed(2)
      priceChange.value = data.solana.usd_24h_change
    }
  } catch (error) {
    console.error('Error fetching SOL price:', error)
    solPrice.value = '---'
  }
}

onMounted(() => {
  fetchSOLPrice()
  // Update every 30 seconds
  priceInterval = setInterval(fetchSOLPrice, 30000)
})

onUnmounted(() => {
  if (priceInterval) {
    clearInterval(priceInterval)
  }
})
</script>

<style scoped>
</style>
