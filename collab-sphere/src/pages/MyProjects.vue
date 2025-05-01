<template>
  <div class="px-8 py-6 max-w-5xl mx-auto">
    <h2 class="text-2xl font-semibold mb-4">My Projects</h2>

    <div class="flex gap-8 mb-6 border-b">
      <button v-for="tab in tabs" :key="tab" @click="activeTab = tab"
        :class="['pb-2 font-medium', activeTab === tab ? 'border-b-2 border-black' : 'text-gray-500']">
        {{ tab }}
      </button>
    </div>

    <div v-if="projects.length" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div v-for="(project, index) in projects" :key="index" class="bg-violet-50 p-5 rounded-2xl space-y-2">
        <!-- Title Section -->
        <div class="flex justify-center items-center gap-2">
          <h3 class="text-lg font-semibold text-black text-center">{{ project.title }}</h3>
          <span :class="[
            'inline-block w-2.5 h-2.5 rounded-full',
            project.status === 'open' ? 'bg-green-500' : 'bg-red-500'
          ]" :title="project.status"></span>
        </div>
        <!-- Description -->
        <p class="text-sm text-gray-600">
          {{ project.description }}
        </p>
        <div class="flex flex-wrap items-center justify-between  text-sm text-gray-600 mb-4 gap-4">
                <!-- Categories -->
                <div class="flex items-center gap-2">
                    <Squares2X2Icon class="w-4 h-4" />
                    <span v-for="(cat, i) in project.categories" :key="i">
                        {{ cat }}<span v-if="i < project.categories.length - 1"> · </span>
                    </span>
                </div>

                <!-- Tags -->
                <div v-if="project.tags.length" class="flex items-center flex-wrap gap-2">
                    <TagIcon class="w-4 h-4" />
                    <span v-for="(tag, i) in project.tags" :key="i"
                        class="bg-violet-100 px-3 py-1 rounded-full text-xs text-purple-700">
                        {{ tag }}
                    </span>
                </div>
            </div>



        

        

  

        <!-- Interest Count and Buttons -->
        <div class="flex justify-between items-center pt-2">
          <div class="text-sm text-gray-500">
            {{ project.interests }} Interested
          </div>
          <div class="flex space-x-3">
            
            <router-link :to="`/project/${project.slug}`" class="bg-purple-600 text-white font-medium text-sm px-3 py-1.5 rounded-md">
              View
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="text-center text-gray-500">
      No projects found.
    </div>
  </div>
</template>

<script>

export default {
  name: 'MyProjects',
  data() {
    return {
      tabs: ['Created', 'Interested'],
      activeTab: 'Created',
      allProjects: [],


    };
  },
  
  watch: {
    activeTab() {
      this.allProjects = [];
      this.fetchProjects();
    }
  },
  computed: {
    projects() {
      return this.allProjects || [];
    },
    iAmAuthor() {
            const user = JSON.parse(localStorage.getItem("user"));
            return this.project && user && this.project.created_by === user.name;
        }
  }, methods: {

    async fetchProjects() {


      try {
        const sortParam = `${this.activeTab.toLowerCase()}`;
        const res = await fetch(
          `http://localhost:5000/api/myprojects?query=${sortParam}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authentication-Token": `${localStorage.getItem("authtoken")}`,
            },
          }
        );
        if (res.status === 401) {
    console.error('Unauthorized access. Please log in.');
    this.$router.push('/signin');
    return;
  }

        if (res.ok) {
          const data = await res.json();
          this.allProjects.push(...data.projects);
          this.totalpages = data.pages; // update from backend
          this.currentpage += 1;
        } else {
          console.error("Failed to fetch projects");
        }
      } catch (err) {
        console.error("Error fetching projects:", err);
      }
    }
  },
  mounted() {
    this.fetchProjects();
  }
}
</script>

<style scoped>
button:focus {
  outline: none;
}
</style>