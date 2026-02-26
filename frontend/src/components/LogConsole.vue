<template>
  <div class="p-4 bg-black bg-opacity-40 rounded-lg glass-effect">
    <h3 class="font-pixel text-lg text-green-300 mb-2">SYSTEM LOGS</h3>
    <pre class="text-sm text-green-300 font-mono h-40 overflow-auto bg-black bg-opacity-60 p-3 rounded">{{ logs.join('\n') }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const logs = ref([
  '[2026-02-26 10:30:01] SNIPER_001: Target lock acquired.',
  '[2026-02-26 10:30:05] ANTIGRAVITY: Gravity anomaly detected (LOW).',
  '[2026-02-26 10:30:20] SNIPER_001: Trade successful. Profit +0.5 SOL.'
])
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
</style>
