<template>
    <nav class="flex items-center justify-between p-4 border-b shadow-sm bg-white relative sticky top-0 z-50">
        <!-- Logo -->
        <router-link to="/"  class="text-xl font-bold text-gray-800">Collab-Sphere</router-link>

        <!-- Desktop Nav -->
        <div class="hidden md:flex items-center space-x-4">
            <template v-if="isAuthenticated">
                <router-link to="/home" class="text-gray-700 hover:text-blue-600">Home</router-link>
                <router-link to="/myprojects" class="text-gray-700 hover:text-blue-600">My projects</router-link>
                <router-link  to="/askai" class="text-gray-700 hover:text-blue-600">Ask AI</router-link>

                <router-link to="/newproject"
                    class="bg-purple-500 hover:bg-purple-600 text-white px-4 py-1.5 rounded-xl shadow">
                    New Project
                </router-link>
                <div class="relative" @click="toggleUserMenu">
                    <UserCircleIcon class="w-8 h-8 rounded-full border-2 border-gray-300 cursor-pointer" />
                    <div v-if="isUserMenuOpen"
                        class="absolute right-0 mt-2 w-32 bg-white border rounded-md shadow-lg z-20">
                        <button @click="logout"
                            class="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-100">
                            Logout
                        </button>
                        
                    </div>
                </div>
            </template>
            <template v-else>
                <router-link to="/signup"
                    class="bg-purple-500 hover:bg-purple-600 text-white px-4 py-1.5 rounded-xl shadow">
                    Sign Up
                </router-link>

                <router-link to="/signin" class="text-gray-700 hover:text-blue-600">
                    Sign In
                </router-link>

            </template>
        </div>

        <!-- Mobile Menu Icon -->
        <div class="md:hidden">
            <button @click="toggleMenu" class="focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M4 6h16M4 12h16M4 18h16" />
                    <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>

        <!-- Mobile Nav -->
        <div v-if="isOpen" class="absolute top-16 left-0 w-full bg-white border-t md:hidden z-10 shadow-md">
            <div class="flex flex-col p-4 space-y-2">
                <template v-if="isAuthenticated">
                    <a href="#" class="text-gray-700 hover:text-blue-600">My projects</a>
                    <a href="#" class="text-gray-700 hover:text-blue-600">Ask AI</a>
                    <button class="bg-purple-500 hover:bg-purple-600 text-white px-4 py-2 rounded-xl shadow">
                        New Project
                    </button>
                    <div class="w-8 h-8 rounded-full bg-blue-200 border-2 border-gray-300 self-center"></div>
                </template>
                <template v-else>
                    <router-link to="/signup"
                        class="bg-purple-500 hover:bg-purple-600 text-white px-4 py-1.5 rounded-xl shadow">
                        Sign Up
                    </router-link>

                    <router-link to="/signin" class="text-gray-700 hover:text-blue-600">
                        Sign In
                    </router-link>
                </template>
            </div>
        </div>
    </nav>
</template>

<script>
import { UserCircleIcon } from '@heroicons/vue/24/solid'
export default {
    name: 'NavBar',

    data() {
        return {
            isOpen: false,

            isUserMenuOpen: false // State for user menu
        };
    },
    computed: {
        isAuthenticated() {
            return this.$store.state.isAuthenticated;
        }
    },
    methods: {
        toggleMenu() {
            this.isOpen = !this.isOpen;
        },
        toggleUserMenu() {
            this.isUserMenuOpen = !this.isUserMenuOpen;
        },
        logout() {
            this.$store.dispatch('logout');
            localStorage.clear();
            this.$router.push('/signin');
        }
    },
    components: {
        UserCircleIcon
    }

}
</script>