<template>
  <section id="tiers" class="py-12">
    <div class="max-w-6xl mx-auto text-center mb-6">
      <h3 class="font-pixel text-3xl text-green-300">Soluciones de Infraestructura</h3>
      <p class="text-muted">Elige una solución alineada a tu escala y necesidades.</p>
    </div>
    <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-6">
      <div class="card p-6">
        <div class="text-lg font-bold">Starter</div>
        <div class="text-2xl text-green-300 mt-2">$0</div>
        <ul class="mt-4 text-muted text-sm">
          <li>Basic scanning</li>
          <li>Community support</li>
        </ul>
        <button class="glitch-btn mt-6 w-full">Select</button>
      </div>
      <div class="card p-6 border-2 border-green-700">
        <div class="text-lg font-bold">Professional</div>
        <div class="text-2xl text-green-300 mt-2">$49/mo</div>
        <ul class="mt-4 text-muted text-sm">
          <li>Realtime sniping</li>
          <li>Antigravity active</li>
        </ul>
        <button class="glitch-btn mt-6 w-full">Select</button>
      </div>
      <div class="card p-6 shadow-neon" style="border:1px solid rgba(255,0,255,0.18)">
        <div class="text-lg font-bold">Elite</div>
        <div class="text-2xl text-fuchsia-400 mt-2">Contact</div>
        <ul class="mt-4 text-muted text-sm">
          <li>Private nodes</li>
          <li>Dedicated support</li>
        </ul>
        <button class="glitch-btn mt-6 w-full" style="background:linear-gradient(90deg,#ff00ff,#00ff7f);">Contact Sales</button>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.text-muted { color: rgba(230,255,242,0.7); }
.card { border-radius: 8px; }
</style>
