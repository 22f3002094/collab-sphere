<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50">
      <div class="text-center">
        <div class="text-4xl font-semibold text-gray-700 mb-4">Coming Soon</div>
        <p class="text-lg text-gray-500 mb-6">Our AI assistant is currently under development.</p>
        <svg class="animate-spin h-8 w-8 text-purple-500 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none"
          viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
          <path class="opacity-75" fill="currentColor"
            d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
        </svg>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "AskAI",
  };
  </script>
  
  <style scoped>
  /* Optional additional styling */
  </style>
  