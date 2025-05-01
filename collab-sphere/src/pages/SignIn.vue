<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
        <div class="max-w-md w-full space-y-6 bg-white p-8 rounded-xl shadow">
            <h2 class="text-2xl font-bold text-gray-900">Welcome Back</h2>
            <p class="text-gray-500">
                Log in to Collab-Sphere to continue contributing to open-source projects.
            </p>

            <!-- Form -->
            <form class="space-y-4" @submit.prevent="signIn">
                <!-- Email -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Email</label>
                    <div class="mt-1 relative rounded-md shadow-sm">
                        <input type="email" placeholder="Enter your email" v-model="email"
                            class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-purple-500 focus:border-purple-500" />
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <EnvelopeIcon class="h-5 w-5 text-gray-400" />
                        </div>
                    </div>
                </div>

                <!-- Password -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Password</label>
                    <div class="mt-1 relative rounded-md shadow-sm">
                        <input type="password" placeholder="Enter your password" v-model="password"
                            class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-purple-500 focus:border-purple-500" />
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <LockClosedIcon class="h-5 w-5 text-gray-400" />
                        </div>
                    </div>
                </div>

                <!-- Button -->
                <button type="submit"
                    class="w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 transition font-semibold">
                    Log In
                </button>
            </form>

            <!-- Link -->
            <p class="text-center text-sm text-gray-500">
                Don't have an account?
                <router-link to="/signup" class="text-blue-600 hover:underline">
                    Sign up
                </router-link>
            </p>
        </div>
    </div>
</template>

<script>
import { EnvelopeIcon, LockClosedIcon } from '@heroicons/vue/24/outline'
export default {
    name: 'SignInPage',
    data() {
        return {
            email: '',
            password: ''
        }
    },
    components: {
        EnvelopeIcon,
        LockClosedIcon
    },
    methods: {
        async signIn() {
            if (this.$store.state.isAuthenticated) {
                this.$router.push('/home');
                return;
            }
            try{

                const backendUrl = 'http://localhost:5000';
                const response = await fetch(`${backendUrl}/api/signin`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: this.email,
                        password: this.password
                    })
                });
                console.log("Request sent");
                console.log("Response status:", response.status);
                if (response.ok) {
                    const data = await response.json();
                    localStorage.setItem('authtoken', data.user.token);
                    localStorage.setItem('user', JSON.stringify(data.user));
                    localStorage.setItem('isAuthenticated', true);
                    this.$store.commit('setUser', data.user);
                    this.$store.commit('setIsAuthenticated', true);
                    console.log("User data:", data.user);
                    if (data.user.onboarding_completed) {
                        this.$router.push('/home');
                    } else {
                        this.$router.push('/home?onboard=true');
                    }
                    
                } else {
                    const error = await response.json();
                    alert(error.message);
                }
            } catch (error) {
                console.error('Error during authentication:', error);
                alert('An error occurred. Please try again.');
            }
        }
    }
}
</script>