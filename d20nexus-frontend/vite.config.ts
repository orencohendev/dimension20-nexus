import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'https://dimension20nexus.com',
        changeOrigin: true,
        secure: false, // if you're connecting to an https server without proper certificates
      },
    },
  },
})