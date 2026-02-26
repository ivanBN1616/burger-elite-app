<template>
  <section id="pricing" class="py-16">
    <div class="max-w-6xl mx-auto text-center mb-8">
      <h3 class="font-pixel text-3xl text-green-300">Pricing</h3>
      <p class="text-gray-300">Elige el nivel que mejor se adapte a tu estrategia.</p>
    </div>
    <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-6">
      <div class="p-6 bg-black bg-opacity-30 rounded-lg text-center">
        <div class="text-xl font-bold mb-2">Free</div>
        <div class="text-4xl text-green-300 mb-4">$0</div>
        <ul class="text-gray-300 text-sm">
          <li>Basic scanning</li>
          <li>Email support</li>
        </ul>
        <button class="mt-6 glitch-btn w-full">Select</button>
      </div>
      <div class="p-6 bg-black bg-opacity-30 rounded-lg text-center border-2 border-green-600">
        <div class="text-xl font-bold mb-2">Pro</div>
        <div class="text-4xl text-green-300 mb-4">$29/mo</div>
        <ul class="text-gray-300 text-sm">
          <li>Realtime sniping</li>
          <li>Priority support</li>
        </ul>
        <button class="mt-6 glitch-btn w-full">Select</button>
      </div>
      <div class="p-6 bg-black bg-opacity-30 rounded-lg text-center hover:shadow-neon hover:scale-105 transition-transform" style="border:1px solid rgba(255,0,255,0.2);">
        <div class="text-xl font-bold mb-2">Elite</div>
        <div class="text-4xl text-fuchsia-400 mb-4">$99/mo</div>
        <ul class="text-gray-300 text-sm">
          <li>All features</li>
          <li>Dedicated bots</li>
        </ul>
        <button class="mt-6 glitch-btn w-full" style="background:linear-gradient(90deg,#ff00ff,#00ff7f);">Select</button>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
.glitch-btn { background: linear-gradient(90deg,#00ff7f,#a100ff); color:#020202; border-radius:12px; padding:10px; }
</style>