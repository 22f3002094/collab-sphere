<template>
  <div class="space-y-6">
    <h2 class="text-2xl font-bold text-center">Preferences & Skills</h2>

    <!-- Interests -->
    <div>
      <div class="relative">
    <input
      v-model="categoryInput"
      @input="filterCategories"
      @keydown.enter.prevent="selectCategory(filteredCategories[0])"
      placeholder="Search or select category"
      class="w-full bg-gray-50 px-4 py-2 rounded focus:outline-none"
    />
    
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
      v-for="(cat, index) in localData.interests"
      :key="index"
      class="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm flex items-center"
    >
      {{ cat }}
      <button @click="removeCategory(index)" class="ml-2 text-xs hover:text-red-600">✕</button>
    </span>
  </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

      <!-- Programming Languages -->
      <div>
        <label class="block text-lg font-semibold mb-1">Programming Languages</label>
        <div class="relative">
          <input v-model="newLanguage" @input="filterlanguage"
            @keydown.enter.prevent="selectlangauage(filteredLanguages[0])"
            placeholder="Search or enter Programming Language"
            class="w-full border rounded-xl px-3 py-1.5 bg-white text-gray-700 placeholder-gray-400" />
          <ul v-if="filteredLanguages.length && newLanguage"
            class="absolute z-10 bg-white border w-full mt-1 rounded shadow">
            <li v-for="tag in filteredLanguages" :key="tag" @click="selectlangauage(tag)"
              class="px-4 py-2 hover:bg-gray-100 cursor-pointer">
              {{ tag }}
            </li>
          </ul>
        </div>
        <div class="flex flex-wrap gap-2 mt-2">
          <span v-for="(tag, index) in localData.programmingLanguages" :key="index"
            class="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm flex items-center">
            {{ tag }}
            <button @click="removelanguage(index)" class="ml-2 text-xs hover:text-red-600">✕</button>
          </span>
        </div>
      </div>


      <!-- Tools -->
      <div>
        <label class="block text-lg font-semibold mb-1">Tools & Technologies</label>
        <div class="relative">
          <input v-model="newTool" @input="filtertool" @keydown.enter.prevent="selecttool(filteredTools[0])"
            placeholder="Search or enter Programming Language"
            class="w-full border rounded-xl px-3 py-1.5 bg-white text-gray-700 placeholder-gray-400" />
          <ul v-if="filteredTools.length && newTool" class="absolute z-10 bg-white border w-full mt-1 rounded shadow">
            <li v-for="tag in filteredTools" :key="tag" @click="selecttool(tag)"
              class="px-4 py-2 hover:bg-gray-100 cursor-pointer">
              {{ tag }}
            </li>
          </ul>
        </div>
        <div class="flex flex-wrap gap-2 mt-2">
          <span v-for="(tag, index) in localData.tools" :key="index"
            class="bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full text-sm flex items-center">
            {{ tag }}
            <button @click="removetool(index)" class="ml-2 text-xs hover:text-red-600">✕</button>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    modelValue: Object
  },
  data() {
    return {
      localData: {
        interests: [...(this.modelValue.interests || [])],
        programmingLanguages: [...(this.modelValue.programmingLanguages || [])],
        tools: [...(this.modelValue.tools || [])]
      },
      
      newLanguage: '',
      newTool: '',
      allTags: [
        "python", "javascript", "react", "vue", "flask", "django", "fastapi", "java",
        "c++", "nodejs", "sql", "mongodb", "firebase", "pandas", "numpy", "tensorflow",
        "pytorch", "api-integration", "docker", "kubernetes", "aws", "gcp", "linux",
        "figma", "html", "css", "tailwind", "openai", "llama", "github-actions", "web3", "solidity"
      ],

      
      filteredLanguages: [],
      filteredTools: [],
      // For categories
    categoryInput: '',
    
    allCategories: [
      'Web Development', 'Mobile Development', 'Data Science', 'Machine Learning', 'AI & LLMs',
      'Cybersecurity', 'Cloud Computing', 'DevOps', 'UI/UX Design', 'Game Development',
      'Blockchain', 'Open Source', 'Competitive Coding', 'IoT & Robotics'
    ],
    filteredCategories: []
      

    };
  },
  watch: {
    localData: {
      deep: true,
      handler() {
        this.updateParent();
      }
    }
  },
  methods: {
    updateParent() {
      this.$emit('update:modelValue', {
        ...this.modelValue,
        ...this.localData
      });
    },


    filterlanguage() {
      const input = this.newLanguage.toLowerCase()
      this.filteredLanguages = this.allTags.filter(
        tag => tag.toLowerCase().includes(input) && !this.localData.programmingLanguages.includes(tag)
      )
    },
    filtertool() {
      const input = this.newTool.toLowerCase()
      this.filteredTools = this.allTags.filter(
        tag => tag.toLowerCase().includes(input) && !this.localData.tools.includes(tag)
      )
    },
    selectlangauage(tag) {
      if (!this.localData.programmingLanguages.includes(tag)) {
        this.localData.programmingLanguages.push(tag)
      }
      this.newLanguage = ''
      this.filteredLanguages = []
    },
    removelanguage(index) {
      this.localData.programmingLanguages.splice(index, 1)
    },
    selecttool(tag) {
      if (!this.localData.tools.includes(tag)) {
        this.localData.tools.push(tag)
      }
      this.newTool = ''
      this.filteredTools = []
    },
    removetool(index) {
      this.localData.tools.splice(index, 1)
    },
    // CATEGORY methods
  filterCategories() {
    const input = this.categoryInput.toLowerCase()
    this.filteredCategories = this.allCategories.filter(
      cat => cat.toLowerCase().includes(input) && !this.localData.interests.includes(cat)
    )
  },
  selectCategory(cat) {
    if (!this.localData.interests.includes(cat)) {
      this.localData.interests.push(cat)
    }
    this.categoryInput = ''
    this.filteredCategories = []
  },
  removeCategory(index) {
    this.localData.interests.splice(index, 1)
  },
  }
};
</script>
