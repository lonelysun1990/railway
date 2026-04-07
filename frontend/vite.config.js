import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 3000,
  },
  preview: {
    port: process.env.PORT ? parseInt(process.env.PORT) : 4173,
  },
})
