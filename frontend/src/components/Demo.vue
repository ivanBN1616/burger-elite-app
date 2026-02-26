<template>
  <section id="demo" class="py-16 text-center">
    <div class="max-w-3xl mx-auto p-6 bg-black bg-opacity-30 rounded-lg">
      <h3 class="font-pixel text-2xl text-green-300 mb-4">Interactive Demo</h3>
      <p class="text-gray-300 mb-4">Simulador: el bot detecta un token basura y lo descarta.</p>
      <div class="mb-4">
        <button @click="runDemo" class="glitch-btn px-6 py-2">Run Simulation</button>
      </div>
      <div class="text-left bg-black bg-opacity-60 p-4 rounded text-sm font-mono text-green-300 h-40 overflow-auto">{{ log }}</div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
const log = ref('')

function append(line){ log.value = (log.value + '\n' + line).trim() }

function runDemo(){
  log.value = ''
  append('[SIM] Scanning token: NEW-XYZ')
  setTimeout(()=> append('[SIM] Antigravity: anomaly detected'), 1000)
  setTimeout(()=> append('[SIM] Token marked as RUG - Discarding'), 2000)
  setTimeout(()=> append('[SIM] Result: No action taken. Wallet safe.'), 3000)
}
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
.glitch-btn { background: linear-gradient(90deg,#00ff7f,#a100ff); color:#020202; border-radius:12px; }
</style>