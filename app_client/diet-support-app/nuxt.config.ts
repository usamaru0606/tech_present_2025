// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  ssr: true,

  css: [
    'vuetify/styles',
    '@mdi/font/css/materialdesignicons.css'
  ],

  build: {
    transpile: ['vuetify'],
  },

  vite: {
    ssr: {
      noExternal: ['vuetify'], 
    },
    server:{
      hmr:{
        protocol:'ws',
        host:'localhost',
        port:3000,
      }
    }
  },

  modules: ['@pinia/nuxt'],
})
