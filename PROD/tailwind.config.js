/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
    './apps/*/templates/**/*.html',
    // Add any other directories where you keep your HTML files or Django template files
  ],
  theme: {
    extend: {},
    spacing: {
      'vertical-menu-sm': '2rem', // Adjust as needed
    },
  },
  plugins: [],
}
