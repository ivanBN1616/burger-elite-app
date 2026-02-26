<template>
  <footer class="py-8 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="mb-4 text-gray-300">Follow us: <a href="#" class="text-green-300">X</a> · <a href="#" class="text-fuchsia-300">Telegram</a> · <a href="#" class="text-green-300">GitHub</a></div>
      <form @submit.prevent="join" class="max-w-md mx-auto flex gap-2">
        <input v-model="email" type="email" placeholder="you@domain.com" class="flex-1 p-2 rounded bg-black bg-opacity-40 text-green-300" required>
        <button class="glitch-btn px-4">Join</button>
      </form>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
const email = ref('')
function join(){ alert('Thanks! We added ' + email.value) }
</script>

<style scoped>
.font-pixel { font-family: 'Press Start 2P', cursive; }
.glitch-btn { background: linear-gradient(90deg,#00ff7f,#a100ff); color:#020202; border-radius:8px; }
</style>