<template>
    <div class="min-h-screen flex justify-center ">
      <div class="bg-white rounded-2xl shadow-lg p-6 w-full max-w-xl">
        <h2 class="text-xl font-bold text-center mb-4">Pending Requests</h2>
        <div v-if="users.length">
        <div v-for="(user, index) in users" :key="index" class="flex items-center justify-between border-b py-3">
          <div class="flex items-center gap-3">
            <UserCircleIcon class="w-10 h-10 rounded-full"></UserCircleIcon>
            <span class="font-semibold text-gray-800">{{ user.username }}</span>
          </div>
          <div class="flex gap-2">
            <button class="px-4 py-1.5 bg-green-500 hover:bg-green-600 text-white rounded-md text-sm">
              Accept
            </button>
            <button class="px-4 py-1.5 bg-red-500 hover:bg-red-600 text-white rounded-md text-sm">
              Reject
            </button>
          </div>
        </div>
      </div>
      <div v-if="users.length === 0" class="text-center text-gray-500">
          No pending requests.
        </div>
        
      </div>
    </div>
  </template>
  
  <script>
  import { UserCircleIcon } from '@heroicons/vue/24/solid'

  export default {
    name: "UserRequestsCard",
    data() {
      return {
        users: [],
      };
    },
    components:{
        UserCircleIcon
    },
    methods: {
      async acceptRequest(user) {
        const slug = this.$route.params.slug;
        try {
          const res = await fetch(`http://localhost:5000/api/utilities?slug=${slug}&action=acceptrequest`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
          });
          if (res.status === 401) {
    console.error('Unauthorized access. Please log in.');
    this.$router.push('/signin');
    return;
  }
          if (res.ok) {
            console.log(`Accepted request from ${user.username}`);
          } else {
            console.error("Failed to accept request");
          }
        } catch (err) {
          console.error("Error accepting request:", err);
        }
      },
      rejectRequest(user) {
        // Logic to reject the request
        console.log(`Rejected request from ${user.username}`);
      },
    },
    async mounted() {
      const slug = this.$route.params.slug;
      try {
            const res = await fetch(`http://localhost:5000/api/utilities?slug=${slug}&action=fetchinterested`,{
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Authentication-Token": `${localStorage.getItem("authtoken")}`,
                },
            });
            if (res.status === 401) {
                console.error('Unauthorized access. Please log in.');
                this.$router.push('/signin');
                return;
            }
            if (res.ok) {
                this.users = await res.json();
                

            } else {
                console.error("Failed to fetch project");
            }
        } catch (err) {
            console.error("Error fetching project:", err);
        }

    },
  };
  </script>
  