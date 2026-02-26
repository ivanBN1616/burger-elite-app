<template>
  <div>
    <Hero />
    <Features />
    <section id="antigravity" class="max-w-6xl mx-auto py-8">
      <div class="p-6 bg-black bg-opacity-40 rounded-lg text-center">
        <h3 class="font-pixel text-2xl text-fuchsia-400 mb-2">Antigravity Feature Showcase</h3>
        <p class="text-gray-300 mb-4">No solo disparamos, aseguramos el aterrizaje.</p>
        <AntigravityRadar />
      </div>
    </section>
    <Pricing />
    <Demo />
    <Footer />
  </div>
</template>

<script setup>
import Hero from '../components/Hero.vue'
import Features from '../components/Features.vue'
import AntigravityRadar from '../components/AntigravityRadar.vue'
import Pricing from '../components/Pricing.vue'
import Demo from '../components/Demo.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
</style>