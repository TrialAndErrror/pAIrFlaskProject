import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

const PORT = 3000;

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000
  }
})
