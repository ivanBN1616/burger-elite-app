<template>
  <div class="p-4 bg-black bg-opacity-40 rounded-lg glass-effect text-center">
    <h3 class="font-pixel text-lg text-fuchsia-400 mb-2">ANTIGRAVITY</h3>
    <div class="mx-auto w-44 h-44 rounded-full relative" :style="radarStyle">
      <div class="absolute inset-0 flex items-center justify-center text-green-300 font-bold">{{ label }}</div>
    </div>
    <button class="mt-4 glitch-btn w-full">Calibrate</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const risk = ref(25)
const label = computed(() => (risk.value > 50 ? `HIGH (${risk.value}%)` : `LOW (${risk.value}%)`))

const radarStyle = computed(() => ({
  border: '2px solid rgba(0,255,0,0.2)',
  background: `conic-gradient(#00FF7F 0% ${risk.value}%, #FF00FF ${risk.value}% 100%)`,
  opacity: 0.85
}))

// Simulate risk update
setInterval(() => { risk.value = (risk.value + 7) % 100 }, 4000)
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
.glitch-btn { background:#00FF7F; color:#050508; padding:8px; border-radius:6px; }
</style>
