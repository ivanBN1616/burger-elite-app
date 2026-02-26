<template>
  <section class="py-8">
    <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="card text-center">
        <div class="text-sm text-muted">Solana TPS</div>
        <div class="text-3xl font-bold text-green-300">2,500</div>
        <div class="text-sm text-muted mt-1">Live network throughput</div>
      </div>
      <div class="card text-center">
        <div class="text-sm text-muted">Average Execution Speed</div>
        <div class="text-3xl font-bold text-green-300">120 ms</div>
        <div class="text-sm text-muted mt-1">From signal to execution</div>
      </div>
      <div class="card text-center">
        <div class="text-sm text-muted">Tokens Analizados Hoy</div>
        <div class="text-3xl font-bold text-fuchsia-400">12,342</div>
        <div class="text-sm text-muted mt-1">Scan pipeline throughput</div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.card { padding: 1rem; border-radius: 0.5rem; }
.text-muted { color: rgba(230,255,242,0.7); }
</style>
