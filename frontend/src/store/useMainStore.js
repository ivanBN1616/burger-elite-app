import { defineStore } from 'pinia'

export const useMainStore = defineStore('main', {
  state: () => ({
    solPrice: 25.67,
    tps: 2500,
    scanners: ['SNIPER','ANTIGRAVITY']
  }),
  actions: {
    setSolPrice(p){ this.solPrice = p }
  }
})
