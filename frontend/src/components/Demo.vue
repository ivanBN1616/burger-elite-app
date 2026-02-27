<template>
  <section id="demo" class="py-24 bg-gradient-to-b from-transparent via-white/[0.01] to-transparent">
    <div class="max-w-4xl mx-auto px-8">
      <div class="mb-12 text-center">
        <h2 class="text-4xl font-light mb-4">Live Simulation</h2>
        <p class="text-gray-500 text-lg font-light">Watch Antigravity detect and reject malicious tokens in real-time</p>
      </div>
      
      <div class="p-8 rounded-lg border border-white/10 glass-effect">
        <div class="mb-6 flex justify-center">
          <button @click="runDemo" class="glitch-btn">Run Simulation</button>
        </div>
        <div class="bg-black/40 p-6 rounded-lg border border-white/10 font-mono text-sm h-64 overflow-auto" style="backdrop-filter: blur(12px);">
          <div v-if="!log" class="text-gray-600 font-light">Click "Run Simulation" to start...</div>
          <div v-else class="space-y-2">
            <div v-for="(line, i) in log.split('\n')" :key="i" class="text-gray-300 font-light">
              <span v-if="line.includes('anomaly detected')" class="text-red-400">{{ line }}</span>
              <span v-else-if="line.includes('safe')" class="text-green-400">{{ line }}</span>
              <span v-else class="text-gray-400">{{ line }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
const log = ref('')

function append(line){ log.value = (log.value + '\n' + line).trim() }

function runDemo(){
  log.value = ''
  append('[SIM] Initializing scan: NEW-XYZ')
  setTimeout(()=> append('[SIM] Analyzing on-chain signals...'), 800)
  setTimeout(()=> append('[SIM] Antigravity: anomaly detected'), 1600)
  setTimeout(()=> append('[SIM] Token flagged as high-risk - REJECTED'), 2400)
  setTimeout(()=> append('[SIM] Result: Transaction aborted. Wallet safe.'), 3200)
}
</script>

<style scoped>
</style>