<template>
    <div>
      <h2 class="text-2xl font-bold mb-6 text-center">Job Info</h2>
  
      <div
        v-for="(job, index) in localData.jobList"
        :key="index"
        class="border rounded-2xl p-6 mb-6 shadow-sm bg-gray-50"
      >
        <div class="grid grid-cols-2 gap-6">
          <div>
            <label class="block text-lg font-semibold mb-1">Company</label>
            <input
              v-model="job.company"
              type="text"
              placeholder="Eg. Google"
              class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400"
            />
          </div>
  
          <div>
            <label class="block text-lg font-semibold mb-1">Position</label>
            <input
              v-model="job.position"
              type="text"
              placeholder="Eg. Software Engineer"
              class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400"
            />
          </div>
  
          <div>
            <label class="block text-lg font-semibold mb-1">Start Date</label>
            <input
              v-model="job.startDate"
              type="date"
              placeholder="Eg. Jan 2021"
              class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400"
            />
          </div>
  
          <div>
            <label class="block text-lg font-semibold mb-1">End Date</label>
            <input
              v-model="job.endDate"
              
              :disabled="job.currentJob"
              :placeholder="job.currentJob ? 'Present' : 'Eg. Dec 2023'"
              type="date"
              class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400 disabled:opacity-60"
            />
          </div>
        </div>
  
        <div class="flex items-center mt-4 space-x-3">
          <input
            type="checkbox"
            v-model="job.currentJob"
            @change="job.currentJob ? job.endDate = '' : null"
            :id="`current-job-${index}`"
          />
          <label :for="`current-job-${index}`" class="text-sm font-medium text-gray-700">
            Currently Working Here
          </label>
  
          <button
            v-if="localData.jobList.length > 1"
            @click="removeJob(index)"
            class="ml-auto text-sm text-red-600 hover:underline"
          >
            Remove
          </button>
        </div>
      </div>
  
      <button
        @click="addJob"
        class="bg-indigo-600 text-white px-4 py-2 rounded-xl text-sm hover:bg-indigo-700"
      >
        + Add Job
      </button>
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
          jobList: this.modelValue.jobList?.length
            ? [...this.modelValue.jobList]
            : [
                {
                  company: '',
                  position: '',
                  startDate: '',
                  endDate: '',
                  currentJob: false
                }
              ]
        }
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
          jobList: [...this.localData.jobList]
        });
      },
      addJob() {
        this.localData.jobList.push({
          company: '',
          position: '',
          startDate: '',
          endDate: '',
          currentJob: false
        });
      },
      removeJob(index) {
        this.localData.jobList.splice(index, 1);
      }
    }
  };
  </script>
  
  <style scoped>
  input[type="checkbox"] {
    width: 1rem;
    height: 1rem;
  }
  </style>
  