<template>
    <div class="border rounded-2xl p-6 mb-6 shadow-sm bg-purple-50">
      <div class="flex justify-between items-center mb-2">
        <div class="flex items-center gap-2 border border-black px-2 py-1 rounded-md text-sm font-medium">
          <EyeIcon class="w-4 h-4" />
          Public
        </div>
        <div class="text-sm text-gray-600">{{ notice.timestamp }}</div>
      </div>
  
      <div class="text-2xl font-semibold mb-1 text-left">{{ notice.title }}</div>
<div class="text-sm text-gray-800 flex items-center gap-1 mb-2 text-left">
  <UserIcon class="w-4 h-4" />
  {{ notice.author }}
</div>

<!-- Content: Slightly indented (e.g., pl-4) -->
<div class="text-gray-700 text-base pl-4 text-left w-full">{{ notice.content }}</div>

  
      <div v-if="!author" class="flex items-center gap-1 mt-3 text-lg font-medium">
        <HandThumbUpIcon class="w-6 h-6" />
        {{ notice.likes }}
      </div>
    </div>
  </template>
  
  <script>
  import { EyeIcon, UserIcon, HandThumbUpIcon } from '@heroicons/vue/24/outline';
  
  export default {
    name: 'NoticeCard',
    props: {
      notice: Object,
      author:Boolean
    },
    components: {
      EyeIcon,
      UserIcon,
      HandThumbUpIcon
    }
  }
  </script>
  