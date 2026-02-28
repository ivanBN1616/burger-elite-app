<template>
  <div class="w-full bg-brand-black">
    <!-- Hero Section with Layered Background -->
    <section class="relative w-full min-h-screen flex items-center justify-center overflow-hidden bg-brand-black pt-24">
      <!-- Base Layer: Technical Background Image -->
      <div
        class="absolute inset-0 w-full h-full bg-cover bg-center"
        style="
          background-image: url('/assets/Gemini_Generated_Image_p3juzfp3juzfp3ju.png');
          filter: brightness(0.6) saturate(0.5);
          opacity: 0.4;
        "
      />

      <!-- Overlay Gradient -->
      <div class="absolute inset-0 bg-gradient-to-b from-brand-black/0 via-brand-black/50 to-brand-black" />

      <!-- Content Layer -->
      <div class="relative z-10 max-w-6xl mx-auto px-4 sm:px-8 text-center">
        <!-- Hero Headline -->
        <h1 class="text-5xl sm:text-7xl md:text-8xl font-light tracking-tight leading-tight mb-6">
          <span class="text-white">DOMINA</span>
          <br />
          <span class="text-brand-green">SOLANA</span>
          <br />
          <span class="text-white">CON BURGER ELITE</span>
        </h1>

        <!-- Hero Subtitle -->
        <p class="text-lg sm:text-xl text-gray-300 max-w-3xl mx-auto mb-8 font-light">
          Sniping en milisegundos con protección Antigravity integrada.
          <br />
          La infraestructura de los traders profesionales.
        </p>

        <!-- CTA Button -->
        <button
          class="px-8 py-4 bg-brand-green text-brand-black font-bold text-lg rounded-lg hover:shadow-neon-strong transition-all duration-300 transform hover:scale-105 mb-12"
        >
          Comenzar Ahora
        </button>

        <!-- Live Network Stats Widget -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center max-w-2xl mx-auto">
          <div class="flex-1 px-6 py-4 border border-white/5 rounded-lg bg-white/5 backdrop-blur-sm hover:border-brand-green/50 transition-colors">
            <p class="text-xs text-gray-400 uppercase tracking-widest mb-1">SOL/USD</p>
            <p class="text-2xl font-bold text-brand-green">$145.32</p>
            <p class="text-xs text-gray-500 mt-1">(live)</p>
          </div>
          <div class="flex-1 px-6 py-4 border border-white/5 rounded-lg bg-white/5 backdrop-blur-sm hover:border-brand-green/50 transition-colors">
            <p class="text-xs text-gray-400 uppercase tracking-widest mb-1">SOL TPS</p>
            <p class="text-2xl font-bold text-brand-green">2,891</p>
          </div>
          <div class="flex-1 px-6 py-4 border border-white/5 rounded-lg bg-white/5 backdrop-blur-sm hover:border-brand-green/50 transition-colors">
            <p class="text-xs text-gray-400 uppercase tracking-widest mb-1">Avg. Execution</p>
            <p class="text-2xl font-bold text-brand-green">0.02s</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Bento Grid: Feature Tiers -->
    <section class="w-full py-20 px-4 sm:px-8 bg-brand-black border-t border-white/5">
      <div class="max-w-7xl mx-auto">
        <h2 class="text-4xl sm:text-5xl font-light text-center mb-16 text-white">
          Elige tu <span class="text-brand-green">infraestructura</span>
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- Starter Tier -->
          <div
            class="group relative p-8 rounded-lg border border-white/5 bg-gradient-to-br from-white/5 to-transparent backdrop-blur-sm hover:border-brand-green/50 hover:shadow-neon transition-all duration-300 transform hover:-translate-y-2"
          >
            <div class="absolute inset-0 bg-gradient-to-br from-brand-green/0 to-brand-green/0 group-hover:from-brand-green/10 group-hover:to-brand-green/5 rounded-lg transition-all duration-300 pointer-events-none" />
            <div class="relative z-10">
              <h3 class="text-2xl font-light text-white mb-1">Sniper Standard</h3>
              <p class="text-xs text-gray-400 uppercase tracking-widest mb-6">entry</p>

              <ul class="space-y-3 text-gray-300 text-sm mb-8">
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">•</span>
                  <span>Entry value</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">•</span>
                  <span>Front-wentgh</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">•</span>
                  <span>Sniper holder</span>
                </li>
              </ul>

              <div class="space-y-2 text-right mb-6">
                <p class="text-sm text-gray-400">Entry value</p>
                <p class="text-3xl font-light text-brand-green">$15,000</p>
              </div>

              <button class="w-full px-4 py-3 border border-brand-green text-brand-green font-bold rounded-lg hover:bg-brand-green hover:text-brand-black transition-all duration-300">
                Get Started
              </button>
            </div>
          </div>

          <!-- Elite Engine Tier (Featured) -->
          <div
            class="group relative p-8 rounded-lg border-2 border-brand-green bg-gradient-to-br from-brand-green/20 to-transparent backdrop-blur-sm shadow-neon-strong transform md:scale-105 hover:-translate-y-2 transition-all duration-300"
          >
            <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-brand-green text-brand-black px-4 py-1 rounded-full text-xs font-bold">
              MOST POPULAR
            </div>
            <div class="relative z-10 mt-4">
              <h3 class="text-2xl font-light text-white mb-1">Elite Engine</h3>
              <p class="text-xs text-gray-300 uppercase tracking-widest mb-6">full access</p>

              <ul class="space-y-3 text-gray-200 text-sm mb-8">
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">✓</span>
                  <span>Full Solana TPS</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">✓</span>
                  <span>Avg. execution cards</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">✓</span>
                  <span>Antigravity Protection</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">✓</span>
                  <span>Priority Queue</span>
                </li>
              </ul>

              <div class="space-y-2 text-right mb-6">
                <p class="text-sm text-gray-300">Avg. Execution</p>
                <p class="text-3xl font-light text-brand-green">0.02s</p>
              </div>

              <button class="w-full px-4 py-3 bg-brand-green text-brand-black font-bold rounded-lg hover:shadow-neon-strong transition-all duration-300 transform hover:scale-105">
                Choose Elite
              </button>
            </div>
          </div>

          <!-- Custom Node Tier -->
          <div
            class="group relative p-8 rounded-lg border border-white/5 bg-gradient-to-br from-white/5 to-transparent backdrop-blur-sm hover:border-brand-green/50 hover:shadow-neon transition-all duration-300 transform hover:-translate-y-2"
          >
            <div class="absolute inset-0 bg-gradient-to-br from-brand-green/0 to-brand-green/0 group-hover:from-brand-green/10 group-hover:to-brand-green/5 rounded-lg transition-all duration-300 pointer-events-none" />
            <div class="relative z-10">
              <h3 class="text-2xl font-light text-white mb-1">Custom Node</h3>
              <p class="text-xs text-gray-400 uppercase tracking-widest mb-6">developers</p>

              <ul class="space-y-3 text-gray-300 text-sm mb-8">
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">•</span>
                  <span>Usite intersection</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">•</span>
                  <span>Elite engine</span>
                </li>
                <li class="flex items-center">
                  <span class="text-brand-green mr-3">•</span>
                  <span>Custom mode</span>
                </li>
              </ul>

              <div class="space-y-2 text-right mb-6">
                <p class="text-sm text-gray-400">Custom infrastructure</p>
                <p class="text-3xl font-light text-brand-green">100F+</p>
              </div>

              <button class="w-full px-4 py-3 border border-brand-green text-brand-green font-bold rounded-lg hover:bg-brand-green hover:text-brand-black transition-all duration-300">
                Request Demo
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Additional Sections -->
    <Hero />
    <Stats />
    <Features />
    <PoweredBy />
    <Docs />
    <Demo />
    <Footer />
  </div>
</template>

<script setup>
import Hero from '../components/Hero.vue'
import Features from '../components/Features.vue'
import Demo from '../components/Demo.vue'
import Footer from '../components/Footer.vue'
import Stats from '../components/Stats.vue'
import PoweredBy from '../components/PoweredBy.vue'
</script>

<style scoped>
/* Subtle grid background pattern (optional enhancement) */
section {
  position: relative;
}

/* Smooth transitions for interactive elements */
button {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }
}
</style>