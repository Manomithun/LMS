import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    plugins: [react()],

    server: {
        host: true,
        allowedHosts: ["library.local"],

        proxy: {
            "/api": {
                target: "http://library.local",
                changeOrigin: false,
                secure: false
            }
        }
    }
});