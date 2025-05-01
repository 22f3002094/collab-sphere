<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
        <div class="max-w-md w-full space-y-6 bg-white p-8 rounded-xl shadow">
            <h2 class="text-2xl font-bold text-gray-900">Create Account</h2>
            <p class="text-gray-500">
                Join Collab-Sphere to discover and contribute to open-source projects.
            </p>

            <!-- Form -->
            <form class="space-y-4" @submit.prevent="signUp">
                <!-- Name -->
                <div>
                    <label class="block text-sm font-medium text-gray-700">Name</label>
                    <div class="mt-1 relative rounded-md shadow-sm">
                        <input type="text" placeholder="Enter your name" v-model="form.name"
                            class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-purple-500 focus:border-purple-500" />
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <UserIcon class="h-5 w-5 text-gray-400" />
                        </div>
                    </div>
                </div>
               

                <div>
                    <label class="block text-sm font-medium text-gray-700">Email</label>
                    <div class="mt-1 relative rounded-md shadow-sm">
                        <input type="email" placeholder="Enter your email" v-model="form.email"
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
                        <input type="password" placeholder="Create a password" v-model="form.password"
                            class="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-purple-500 focus:border-purple-500" />
                        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                            <LockClosedIcon class="h-5 w-5 text-gray-400" />
                        </div>
                    </div>
                </div>

                <!-- Button -->
                <button type="submit"
                    class="w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700 transition font-semibold">
                    Sign Up
                </button>
            </form>

            <!-- Link -->
            <p class="text-center text-sm text-gray-500">
                Already have an account?
                <router-link to="/signin" class="text-blue-600 hover:underline">
                    Sign in
                </router-link>
            </p>
        </div>
    </div>
</template>

<script>
import { UserIcon, EnvelopeIcon, LockClosedIcon } from '@heroicons/vue/24/outline'

export default {
    components: {
        UserIcon,
        EnvelopeIcon,
        LockClosedIcon,
       
    }, data() {
        return {
            form: {
                name: '',
                email: '',
                password: '',
                username: '',
            },
            usernameAvailable: null, 
            checkingUsername: false, 
        }
    },
    watch: {
        'form.username'() {
            this.debouncedCheckUsername(); // 🔥 Trigger debounced check
        }
    },
    created() {
        this.debouncedCheckUsername = this.debounce(this.checkUsernameAvailability, 500); // 🔥 Add debounce
    },
    methods: {
        async checkUsernameAvailability() {
            const username = this.form.username.trim();
            if (!username) {
                this.usernameAvailable = null;
                return;
            }

            this.checkingUsername = true;
            try {
                const res = await fetch('http://localhost:5000/api/user?action=checkusername', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ username }),
                });

                const data = await res.json();
                this.usernameAvailable = !data.exists; 
                console.log("Username check response:", data);

            } catch (err) {
                console.error('Username check failed:', err);
                this.usernameAvailable = null;
            } finally {
                this.checkingUsername = false;
            }
        },

        debounce(fn, delay) {
            let timeout;
            return (...args) => {
                clearTimeout(timeout);
                timeout = setTimeout(() => fn.apply(this, args), delay);
            };
        },

        async signUp() {
            if (this.usernameAvailable === false) {
                alert("Username is already taken.");
                return;
            }

            try {
                const response = await fetch(`${this.$globaldata.backendUrl}/api/signup`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(this.form)
                });

                if (response.status !== 201) {
                    throw new Error("Failed to Sign Up");
                }

                const data = await response.json();
                if (data.message) {
                    this.$router.push("/signin");
                } else {
                    alert(data.message || "Authentication failed");
                }
            } catch (error) {
                console.error("Error during authentication:", error);
            }
        }

    },
}
</script>