<template>
  <div class="p-4 bg-black bg-opacity-40 rounded-lg glass-effect">
    <h3 class="font-pixel text-xl text-green-300 mb-4">SNIPER MONITOR</h3>
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-gray-300">
          <th>Token</th>
          <th>Price</th>
          <th>Change</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="t in tokens" :key="t.symbol" class="border-t border-gray-700">
          <td>{{ t.symbol }}</td>
          <td>{{ t.price }}</td>
          <td :class="t.change>0? 'text-green-400':'text-fuchsia-400'">{{ t.change }}%</td>
          <td>{{ t.status }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const tokens = ref([
  { symbol: 'BURGER', price: '0.012', change: 2.3, status: 'Active' },
  { symbol: 'SNIP', price: '0.45', change: -1.2, status: 'Idle' }
])
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
</style>
