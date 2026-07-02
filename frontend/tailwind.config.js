/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'neo-yellow': '#FFE800',
        'neo-pink': '#FF007F',
        'neo-cyan': '#00E5FF',
        'neo-green': '#00FF00',
      },
      boxShadow: {
        'neo-sm': '4px 4px 0px 0px rgba(0,0,0,1)',
        'neo-md': '6px 6px 0px 0px rgba(0,0,0,1)',
        'neo-lg': '8px 8px 0px 0px rgba(0,0,0,1)',
      }
    },
  },
  plugins: [],
}
