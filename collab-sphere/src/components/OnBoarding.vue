<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="bg-white rounded-3xl shadow-xl p-8 w-full max-w-3xl relative border border-gray-200">

      <!-- Progress Tracker -->
      <div class="relative mb-10 px-6">
        <!-- Full Gray Line -->
        <div class="absolute top-1/2 left-4 right-4 h-1 bg-gray-200 rounded-full z-0 transform -translate-y-1/2"></div>

        <!-- Filled Progress Line -->
        <div
          class="absolute top-1/2 left-4 h-1 bg-purple-500 rounded-full z-10 transform -translate-y-1/2 transition-all duration-300"
          :style="{ width: trackFillWidth }"></div>

        <!-- Steps -->
        <div class="flex justify-between relative z-20">
          <template v-for="(step, index) in steps" :key="index">
            <div class="flex flex-col items-center relative z-30">
              <div
                class="w-8 h-8 flex items-center justify-center rounded-full border-2 text-sm font-semibold transition-all duration-300"
                :class="{
                  'bg-purple-500 text-white border-purple-500': index <= currentStep,
                  'bg-white text-gray-400 border-gray-300': index > currentStep
                }">
                {{ index + 1 }}
              </div>
            </div>
          </template>
        </div>
      </div>

      <!-- Dynamic Step Content -->
      <component :is="steps[currentStep].component" v-model="formData" />

      <!-- Navigation Buttons -->
      <div class="flex justify-between mt-8">
        <button v-if="currentStep > 0" @click="prevStep"
          class="px-4 py-2 bg-gray-300 text-gray-700 rounded-xl text-sm hover:bg-gray-400 transition">
          Back
        </button>
        <button @click="nextStep"
          class="bg-purple-500 hover:bg-purple-600 text-white ml-auto px-6 py-1.5 rounded-xl shadow">
          {{ currentStep === steps.length - 1 ? 'Finish' : 'Next' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import PersonalInfo from './PersonalInfo.vue'
import PreferenceInfo from './PreferenceInfo.vue'
import EducationalInfo from './EducationalInfo.vue'
import JobInfo from './JobInfo.vue'
import AllSummary from './AllSummary.vue'


export default {
  components: {
    PersonalInfo,
    PreferenceInfo,
    EducationalInfo,
    JobInfo,
    AllSummary
  },
  data() {
    return {
      currentStep: 0,
      formData: {
        personalinfo: {
          firstname: "",
          lastname: "",
          age: "",
          gender: "",
          city: "",
          country: "",
          github: "",
          linkedin: "",
          website: "",
          bio: ""
        },

        educationList: [
          {
            institution: '',
            degree: '',
            startYear: '',
            endYear: '',
            present: false
          }
        ]
        ,
        jobList: [
          {
            company: '',
            position: '',
            startDate: '',
            endDate: '',
            currentJob: false
          }
        ],
        preferencesAndSkills: {
          interests: [],              // e.g., "AI, Web Development, Open Source"
          programmingLanguages: [],   // e.g., ["JavaScript", "Python"]
          tools: []                   // e.g., ["VS Code", "Git", "Docker"]
        }
      },

      steps: [
        { title: 'Your Personal Info', component: 'PersonalInfo' },
        { title: 'Your Educational Info', component: 'EducationalInfo' },
        { title: 'Your Job Info', component: 'JobInfo' },
        { title: 'Your Preferance', component: 'PreferenceInfo' },
        { title: 'All the summary', component: 'AllSummary' }
      ]
    }
  },
  computed: {
    trackFillWidth() {
      if (this.currentStep === 0) return '0%';
      const percentage = ((this.currentStep) / (this.steps.length - 1)) * 100;
      return `${percentage}%`;
    }
  },
  methods: {
    nextStep() {
      if (this.currentStep < this.steps.length - 1) {
        this.currentStep++;
      } else {
        this.submitData();
      }
    },
    prevStep() {
      if (this.currentStep > 0) {
        this.currentStep--;
      }
    },
    async submitData() {
      try {
        console.log("Submitting data:", this.formData);
        const response = await fetch("http://127.0.0.1:5000/api/user-profile", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authentication-Token": localStorage.getItem("authtoken")
          },
          body: JSON.stringify(this.formData)
        });
        if (response.status === 401) {
    console.error('Unauthorized access. Please log in.');
    this.$router.push('/signin');
    return;
  }

        if (!response.ok) {
          const errorData = await response.json();
          console.error("Error response:", errorData);
          alert(`Error: ${errorData.message || "An error occurred"}`);
          return;
        }

        const result = await response.json();
        console.log("Submission successful:", result);
        this.$router.push("/home");
      } catch (error) {
        console.error("Submission error:", error);
        alert(`Error: ${error.message || "An unexpected error occurred"}`);
      }
    }
  }
}
</script>