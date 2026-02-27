<template>
  <footer class="py-16 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-8">
      <div class="grid md:grid-cols-2 gap-12 mb-12">
        <div>
          <div class="text-xl font-light mb-4">BURGER ELITE</div>
          <p class="text-gray-500 font-light max-w-sm">Enterprise infrastructure for Solana trading. Built for speed, security, and scale.</p>
        </div>
        <div class="grid grid-cols-2 gap-8">
          <div>
            <div class="text-sm text-gray-500 uppercase tracking-wider mb-4">Product</div>
            <div class="space-y-2">
              <a href="#features" class="block text-sm text-gray-400 hover:text-white transition-colors duration-300">Features</a>
              <a href="#tiers" class="block text-sm text-gray-400 hover:text-white transition-colors duration-300">Pricing</a>
              <a href="#docs" class="block text-sm text-gray-400 hover:text-white transition-colors duration-300">Documentation</a>
            </div>
          </div>
          <div>
            <div class="text-sm text-gray-500 uppercase tracking-wider mb-4">Connect</div>
            <div class="space-y-2">
              <a href="#" class="block text-sm text-gray-400 hover:text-white transition-colors duration-300">X / Twitter</a>
              <a href="#" class="block text-sm text-gray-400 hover:text-white transition-colors duration-300">Telegram</a>
              <a href="#" class="block text-sm text-gray-400 hover:text-white transition-colors duration-300">GitHub</a>
            </div>
          </div>
        </div>
      </div>
      <div class="pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center">
        <div class="text-sm text-gray-500">© 2026 Burger Elite. All rights reserved.</div>
        <form @submit.prevent="join" class="flex gap-2 mt-4 md:mt-0">
          <input v-model="email" type="email" placeholder="your@email.com" class="px-4 py-2 rounded-md bg-white/5 border border-white/10 text-sm focus:outline-none focus:border-white/20 transition-colors duration-300" required>
          <button class="px-6 py-2 rounded-md bg-white/10 hover:bg-white/15 border border-white/10 text-sm transition-all duration-300">Subscribe</button>
        </form>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
const email = ref('')
function join(){ alert('Thanks! We added ' + email.value) }
</script>

<style scoped>
</style>