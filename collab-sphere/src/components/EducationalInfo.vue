<template>
  <div>
    <h2 class="text-2xl font-bold mb-6 text-center">Educational Info</h2>

    <div
      v-for="(edu, index) in localData.educationList"
      :key="index"
      class="border rounded-2xl p-6 mb-6 shadow-sm bg-gray-50"
    >
      <div class="grid grid-cols-2 gap-6">
        <div>
          <label class="block text-lg font-semibold mb-1">Institution</label>
          <input
            v-model="edu.institution"
            type="text"
            placeholder="Eg. Harvard University"
            class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400"
          />
        </div>

        <div>
          <label class="block text-lg font-semibold mb-1">Degree</label>
          <input
            v-model="edu.degree"
            type="text"
            placeholder="Eg. B.Sc Computer Science"
            class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400"
          />
        </div>

        <div>
          <label class="block text-lg font-semibold mb-1">Start Year</label>
          <input
            v-model="edu.startYear"
            type="date"
            placeholder="Eg. 2018"
            class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400"
          />
        </div>

        <div>
          <label class="block text-lg font-semibold mb-1">End Year</label>
          <input
            v-model="edu.endYear"
            :disabled="edu.present"
            :placeholder="edu.present ? 'Present' : 'Eg. 2022'"
            type="date"
            class="w-full border rounded-xl px-4 py-2 bg-white text-gray-700 placeholder-gray-400 disabled:opacity-60"
          />
        </div>
      </div>

      <div class="flex items-center mt-4 space-x-3">
        <input
          type="checkbox"
          v-model="edu.present"
          @change="edu.present ? edu.endYear = '' : null"
          :id="`present-checkbox-${index}`"
        />
        <label :for="`present-checkbox-${index}`" class="text-sm font-medium text-gray-700">
          Currently Studying
        </label>

        <button
          v-if="localData.educationList.length > 1"
          @click="removeEducation(index)"
          class="ml-auto text-sm text-red-600 hover:underline"
        >
          Remove
        </button>
      </div>
    </div>

    <button
      @click="addEducation"
      class="bg-indigo-600 text-white px-4 py-2 rounded-xl text-sm hover:bg-indigo-700"
    >
      + Add Education
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
        educationList: this.modelValue.educationList?.length
          ? [...this.modelValue.educationList]
          : [
              {
                institution: '',
                degree: '',
                startYear: '',
                endYear: '',
                present: false
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
        educationList: [...this.localData.educationList]
      });
    },
    addEducation() {
      this.localData.educationList.push({
        institution: '',
        degree: '',
        startYear: '',
        endYear: '',
        present: false
      });
    },
    removeEducation(index) {
      this.localData.educationList.splice(index, 1);
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
