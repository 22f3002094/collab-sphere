<template>
  <div class="max-w-2xl mx-auto py-10 px-6">
    <h2 class="text-2xl font-semibold mb-6">Post a Project</h2>

    <!-- Project Title -->
    <div class="mb-4">
      <label class="block mb-1 font-medium">Project Title</label>
      <div class="flex items-center bg-gray-50 px-4 py-2 rounded">
        <input v-model="title" type="text" placeholder="Enter your project name"
          class="bg-transparent w-full focus:outline-none" />
        <span class="text-gray-500 font-bold text-lg">T</span>


      </div>
    </div>

    <!-- Description -->
    <div class="mb-4">
      <label class="block mb-1 font-medium">Description</label>
      <textarea v-model="description" rows="4" placeholder="Describe your project idea and goals"
        class="w-full px-4 py-2 bg-gray-50 rounded focus:outline-none resize-none"></textarea>
    </div>


    <!-- Category -->
<div class="mb-6">
  <label class="block mb-1 font-medium">Category</label>
  <div class="relative">
    <input
      v-model="categoryInput"
      @input="filterCategories"
      @keydown.enter.prevent="selectCategory(filteredCategories[0])"
      placeholder="Search or select category"
      class="w-full bg-gray-50 px-4 py-2 rounded focus:outline-none"
    />
    <Squares2X2Icon class="w-5 h-5 text-gray-400 absolute right-3 top-1/2 transform -translate-y-1/2 pointer-events-none" />
    <!-- Dropdown -->
    <ul v-if="filteredCategories.length && categoryInput" class="absolute z-10 bg-white border w-full mt-1 rounded shadow">
      <li
        v-for="cat in filteredCategories"
        :key="cat"
        @click="selectCategory(cat)"
        class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
      >
        {{ cat }}
      </li>
    </ul>
  </div>
  <div class="flex flex-wrap gap-2 mt-2">
    <span
      v-for="(cat, index) in selectedCategories"
      :key="index"
      class="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm flex items-center"
    >
      {{ cat }}
      <button @click="removeCategory(index)" class="ml-2 text-xs hover:text-red-600">✕</button>
    </span>
  </div>
</div>




    <!-- Tags -->
<div class="mb-4">
  <label class="block mb-1 font-medium">Tags</label>
  <div class="relative">
    <input
      v-model="tagInput"
      @input="filterTags"
      @keydown.enter.prevent="selectTag(filteredTags[0])"
      placeholder="Search or enter tag"
      class="w-full bg-gray-50 px-4 py-2 rounded focus:outline-none"
    />
    <TagIcon class="w-5 h-5 text-gray-400 absolute right-3 top-1/2 transform -translate-y-1/2 pointer-events-none" />

    <!-- Dropdown -->
    <ul v-if="filteredTags.length && tagInput" class="absolute z-10 bg-white border w-full mt-1 rounded shadow">
      <li
        v-for="tag in filteredTags"
        :key="tag"
        @click="selectTag(tag)"
        class="px-4 py-2 hover:bg-gray-100 cursor-pointer"
      >
        {{ tag }}
      </li>
    </ul>
  </div>
  <div class="flex flex-wrap gap-2 mt-2">
    <span
      v-for="(tag, index) in selectedTags"
      :key="index"
      class="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm flex items-center"
    >
      {{ tag }}
      <button @click="removeTag(index)" class="ml-2 text-xs hover:text-red-600">✕</button>
    </span>
  </div>
</div>


    <!-- Post Button -->
    <button @click="submitForm" class="bg-purple-600 text-white px-6 py-2 rounded-full hover:bg-purple-700 transition">
      Post Project
    </button>
  </div>
</template>

<script>
import { TagIcon, Squares2X2Icon } from '@heroicons/vue/24/outline'

export default {
  name: 'NewProject',
  components: {
    TagIcon,
    Squares2X2Icon
  },
  data() {
  return {
    title: '',
    description: '',

    // For tags
    tagInput: '',
    selectedTags: [],
    allTags: [
      "python", "javascript", "react", "vue", "flask", "django", "fastapi", "java",
      "c++", "nodejs", "sql", "mongodb", "firebase", "pandas", "numpy", "tensorflow",
      "pytorch", "api-integration", "docker", "kubernetes", "aws", "gcp", "linux",
      "figma", "html", "css", "tailwind", "openai", "llama", "github-actions", "web3", "solidity"
    ],
    filteredTags: [],

    // For categories
    categoryInput: '',
    selectedCategories: [],
    allCategories: [
      'Web Development', 'Mobile Development', 'Data Science', 'Machine Learning', 'AI & LLMs',
      'Cybersecurity', 'Cloud Computing', 'DevOps', 'UI/UX Design', 'Game Development',
      'Blockchain', 'Open Source', 'Competitive Coding', 'IoT & Robotics'
    ],
    filteredCategories: []
  }
},
methods: {
  // CATEGORY methods
  filterCategories() {
    const input = this.categoryInput.toLowerCase()
    this.filteredCategories = this.allCategories.filter(
      cat => cat.toLowerCase().includes(input) && !this.selectedCategories.includes(cat)
    )
  },
  selectCategory(cat) {
    if (!this.selectedCategories.includes(cat)) {
      this.selectedCategories.push(cat)
    }
    this.categoryInput = ''
    this.filteredCategories = []
  },
  removeCategory(index) {
    this.selectedCategories.splice(index, 1)
  },

  // TAG methods
  filterTags() {
    const input = this.tagInput.toLowerCase()
    this.filteredTags = this.allTags.filter(
      tag => tag.toLowerCase().includes(input) && !this.selectedTags.includes(tag)
    )
  },
  selectTag(tag) {
    if (!this.selectedTags.includes(tag)) {
      this.selectedTags.push(tag)
    }
    this.tagInput = ''
    this.filteredTags = []
  },
  removeTag(index) {
    this.selectedTags.splice(index, 1)
  },

  // Submit
  async submitForm() {
  const payload = {
    title: this.title,
    description: this.description,
    tags: this.selectedTags,
    categories: this.selectedCategories
  };

  try {
    const response = await fetch('http://localhost:5000/api/project', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authentication-Token': localStorage.getItem('authtoken')
      },
      body: JSON.stringify(payload)
    });
    if (response.status === 401) {
    console.error('Unauthorized access. Please log in.');
    this.$router.push('/signin');
    return;
  }
    if (!response.ok) {
      throw new Error('Failed to submit project');
    }

    const result = await response.json();
    console.log('Project submitted successfully:', result);

    // Optional: Clear form or show success message
    this.title = '';
    this.description = '';
    this.tags = [];
    this.selectedCategories = [];
    this.tagInput = '';
    this.categoryInput = '';
    
    // alert('Project posted successfully!');
    this.$router.push('/home'); // Redirect to home or another page
  } catch (error) {
    console.error('Error:', error);
    alert('There was an error submitting the project.');
  }
}

}
}

</script>