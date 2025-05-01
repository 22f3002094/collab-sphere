<template>
    <div>

      <div class="flex items-center justify-center min-h-screen bg-white px-4 text-center">
        <div class="max-w-2xl">
          <h1 class="text-4xl md:text-5xl font-bold text-gray-800 mb-6">
            {{ welcome }}
          </h1>
          <p class="text-lg md:text-xl text-gray-600 leading-relaxed">
            Find and join beginner-friendly open-source projects. <br />
            Share your ideas, connect with collaborators, <br />
            and start building together.
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>

  
  export default {
    
    data() {
      return {
        welcome: 'Welcome to Collab-Sphere',
      }
    },
    mounted(){
        if(localStorage.getItem('authtoken')){
          console.log('Token found')
            this.$router.push('/home')
        }
        console.log('Token not found')
      
    }
  }
  </script>
  