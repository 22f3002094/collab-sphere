<template>
  <div class="px-8 py-6 max-w-5xl mx-auto">
    <!-- Heading -->
    <h2 class="text-2xl font-semibold mb-2">Explore Projects</h2>

    <div class="flex space-x-6 border-b mb-6 text-sm font-medium text-gray-600">
      <button v-for="tab in tabs" :key="tab" @click="changeTab(tab)"
        :class="['pb-2', activeTab === tab ? 'border-b-2 border-black text-black' : 'hover:text-black']">
        {{ tab }}
      </button>
    </div>


    <!-- Project Cards -->
<div class="space-y-4">
  <div v-for="(project, index) in projects" :key="index" class="bg-violet-50 p-5 rounded-2xl space-y-2">
    
    <!-- Category & Creator -->
    <div class="flex items-center justify-between text-sm text-gray-600">
      <div class="flex items-center space-x-2">
        <span v-for="(cat, i) in project.categories" :key="i">{{ cat }}<span v-if="i < project.categories.length - 1"> · </span></span>
      </div>
      <span v-if="project.created_by" class="italic text-gray-500">by {{ project.created_by }}</span>
    </div>

    <!-- Title -->
    <h3 class="text-lg font-semibold text-black">{{ project.title }}</h3>

    <!-- Description -->
    <p class="text-sm text-gray-600">
      {{ project.description }}
    </p>

    <!-- Tags -->
    <div v-if="project.tags.length" class="flex flex-wrap gap-2 text-xs text-purple-700">
      <span
        v-for="(tag, i) in project.tags"
        :key="i"
        class="bg-violet-100 px-2 py-0.5 rounded-full"
      >
        {{ tag }}
      </span>
    </div>

    <!-- Interest Count and Buttons -->
    <div class="flex justify-between items-center pt-2">
      <div class="text-sm text-gray-500">
        {{ project.interests }} Interested
      </div>
      <div class="flex space-x-3">
        <div v-if="project.interested_by_user" class="flex space-x-3">
                        <button class="bg-purple-600 text-white font-semibold text-sm px-3 py-1.5 rounded-md">
                            Marked as Interested
                        </button>
                    </div>
                    <div v-else class="flex space-x-3">
                        <button @click="show_interest"
                            class="bg-purple-600 text-white font-semibold text-sm px-3 py-1.5 rounded-md">
                            I'm Interested
                        </button>
                    </div>
        <router-link :to="`/project/${project.slug}`" class="bg-violet-100 text-purple-700 font-medium text-sm px-3 py-1.5 rounded-md">
          View
        </router-link>
      </div>
    </div>
  </div>
</div>

    <div v-if="loading" class="flex justify-center py-4">
      <svg class="animate-spin h-6 w-6 text-purple-600" xmlns="http://www.w3.org/2000/svg" fill="none"
        viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
      </svg>
    </div>
    <div v-if="!loading && currentpage > totalpages" class="text-center text-sm text-gray-500 mt-4">
      🎉 You've reached the end of the feed.
    </div>
  </div>

</template>

<script>


export default {
  name: "FeedPage",
  
  data() {
    return {
      tabs: ['All'],
      activeTab: 'All',
      projects: [],
      currentpage: 1,
      totalpages: 1,
      itemsPerPage: 3,
      loading: false,
    };
  },
  methods: {
    async fetchProjects() {
      if (this.loading || this.currentpage > this.totalpages) return;
      this.loading = true;

      try {
        const sortParam = this.activeTab !== 'All' ? `&sort=${this.activeTab.toLowerCase()}` : '';
        const res = await fetch(
          `http://localhost:5000/api/feed?page=${this.currentpage}&per_page=${this.itemsPerPage}${sortParam}`,
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
          this.projects.push(...data.projects);
          this.totalpages = data.pages; // update from backend
          this.currentpage += 1;
        } else {
          console.error("Failed to fetch projects");
        }
      } catch (err) {
        console.error("Error fetching projects:", err);
      } finally {
        this.loading = false;
      }
    },
    handleScroll() {
      const scrollY = window.scrollY;
      const windowHeight = window.innerHeight;
      const bodyHeight = document.body.offsetHeight;

      // If near bottom and more pages are left
      if (scrollY + windowHeight >= bodyHeight - 100 && this.currentpage <= this.totalpages) {
        this.fetchProjects();
      }
    },
    changeTab(tab) {
    if (tab !== this.activeTab) {
      this.activeTab = tab;
      this.projects = [];
      this.currentpage = 1;
      this.totalpages = 1;
      this.fetchProjects();
    }
  },
  async show_interest(project) {
            const projectslug = project.slug;
            
            try {
                const res = await fetch(`http://localhost:5000/api/utilities?action=showinterest&slug=${projectslug}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authentication-Token': `${localStorage.getItem("authtoken")}`
                    }
                });
                if (res.ok) {
                    
                    this.$router.go(0);
                } else if (res.status === 401) {
                    console.error('Unauthorized access. Please log in.');
                    this.$router.push('/signin');
                }else {
                    console.error("Failed to mark interest");
                }
            } catch (err) {
                console.error("Error marking interest:", err);
            }
        },
  },
  mounted() {
    this.fetchProjects();
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  

};
</script>
