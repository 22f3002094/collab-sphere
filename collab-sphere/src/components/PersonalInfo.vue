<template>
  <div class="space-y-6">
    <h2 class="text-2xl font-bold mb-6 text-center">Personal Info</h2>

    <div class="grid grid-cols-2 gap-6">
      <div>
        <label class="block text-lg font-semibold mb-1">First Name</label>
        <input
          type="text"
          v-model="localData.firstname"
          placeholder="Eg. John"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>
      <div>
        <label class="block text-lg font-semibold mb-1">Last Name</label>
        <input
          type="text"
          v-model="localData.lastname"
          placeholder="Eg. Doe"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>
      <div>
        <label class="block text-lg font-semibold mb-1">Age</label>
        <input
          type="text"
          v-model="localData.age"
          placeholder="Eg. 22"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>
      <div>
        <label class="block text-lg font-semibold mb-1">Gender</label>
        <input
          type="text"
          v-model="localData.gender"
          placeholder="Eg. Male, Female"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>
      <div>
        <label class="block text-lg font-semibold mb-1">City</label>
        <input
          type="text"
          v-model="localData.city"
          placeholder="Eg. Delhi"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>
      <div>
        <label class="block text-lg font-semibold mb-1">Country</label>
        <input
          type="text"
          v-model="localData.country"
          placeholder="Eg. India"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>
    </div>

    <div>
      <label class="block text-lg font-semibold mb-1">Bio</label>
      <textarea
        v-model="localData.bio"
        placeholder="A short personal summary..."
        rows="4"
        class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
      ></textarea>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="flex items-center gap-2">
        <svg class="w-5 h-5 text-gray-500" fill="currentColor" viewBox="0 0 24 24">
          <path
            d="M12 0C5.37 0 0 5.373 0 12c0 5.303 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.84 1.237 1.84 1.237 1.07 1.834 2.807 1.304 3.492.996.108-.776.42-1.305.763-1.605-2.665-.305-5.466-1.332-5.466-5.93 0-1.31.47-2.381 1.237-3.221-.124-.303-.536-1.524.117-3.176 0 0 1.008-.322 3.3 1.23.957-.266 1.984-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.29-1.552 3.296-1.23 3.296-1.23.655 1.653.243 2.874.12 3.176.77.84 1.235 1.911 1.235 3.221 0 4.61-2.805 5.624-5.476 5.921.431.372.815 1.102.815 2.222v3.293c0 .322.216.694.825.576C20.565 21.796 24 17.302 24 12c0-6.627-5.373-12-12-12z"
          />
        </svg>
        <input
          type="url"
          v-model="localData.github"
          placeholder="GitHub Profile URL"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>

      <div class="flex items-center gap-2">
        <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 24 24">
          <path
            d="M19 0h-14c-2.76 0-5 2.24-5 5v14c0 2.76 2.24 5 5 5h14c2.76 0 5-2.24 5-5v-14c0-2.76-2.24-5-5-5zm-11.5 19h-3v-10h3v10zm-1.5-11.28c-.966 0-1.75-.79-1.75-1.76s.784-1.75 1.75-1.75 1.75.79 1.75 1.75-.784 1.76-1.75 1.76zm13.5 11.28h-3v-5.6c0-3.356-4-3.1-4 0v5.6h-3v-10h3v1.3c1.396-2.586 7-2.777 7 2.476v6.224z"
          />
        </svg>
        <input
          type="url"
          v-model="localData.linkedin"
          placeholder="LinkedIn Profile URL"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
      </div>

      <div class="md:col-span-2">
        <label class="block text-lg font-semibold mb-1">Portfolio Website</label>
        <input
          type="url"
          v-model="localData.website"
          placeholder="https://your-portfolio.com"
          class="w-full border rounded-xl px-4 py-2 bg-gray-50 text-gray-700 placeholder-gray-400"
        />
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
      localData: { ...this.modelValue.personalinfo }
    };
  },
  watch: {
    localData: {
      handler() {
        this.updateParent();
      },
      deep: true
    }
  },
  methods: {
    updateParent() {
      const updated = {
        ...this.modelValue,
        personalinfo: { ...this.localData }
      };
      this.$emit('update:modelValue', updated);
    }
  }
};
</script>
