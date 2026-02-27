import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,
    // Allow the domain and its www subdomain to access the dev server
    allowedHosts: ['burger-elite.com', 'www.burger-elite.com', '46.225.109.134'],
  },
})
