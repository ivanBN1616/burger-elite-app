<template>
  <section class="py-12">
    <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-8 items-center">
      <div>
        <h3 class="font-pixel text-2xl text-fuchsia-400 mb-2">Powered by Antigravity</h3>
        <p class="text-muted mb-4">Nuestro filtro de seguridad inspecciona cada orden antes de enviarla a la red. Filtrado por señales, reputación y heurísticas on-chain.</p>
        <ul class="text-sm text-muted space-y-2">
          <li>• Multi-layer checks (heuristics, Mempool, Helius)</li>
          <li>• Real-time anomaly detection</li>
          <li>• Fail-safe abort antes de cualquier ejecución sospechosa</li>
        </ul>
      </div>
      <div class="card p-6 flex items-center justify-center">
        <!-- Simple SVG diagram placeholder -->
        <svg width="320" height="180" viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
          <rect x="0" y="0" width="320" height="180" rx="8" fill="#020204" stroke="#0b0b0c" />
          <g fill="none" stroke="#00FF7F" stroke-width="2">
            <path d="M10 90 L90 30 L170 90 L250 30 L310 90" stroke-opacity="0.18"/>
            <circle cx="90" cy="30" r="6" fill="#00FF7F"/>
            <circle cx="170" cy="90" r="6" fill="#FF00FF"/>
            <circle cx="250" cy="30" r="6" fill="#00FF7F"/>
          </g>
          <text x="160" y="160" font-size="11" text-anchor="middle" fill="#9ca3af">Traffic passes through Antigravity filter</text>
        </svg>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.text-muted { color: rgba(230,255,242,0.7); }
.card { background: rgba(10,10,12,0.7); border-radius: 8px; }
</style>
