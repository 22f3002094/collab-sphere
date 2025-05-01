<template>
    <div class="max-w-5xl mx-auto p-6 bg-white rounded-xl shadow-md">
      <!-- Header Section -->
      <div class="bg-violet-50 rounded-t-xl mb-6">
  <div class="flex items-center space-x-6 p-6">
    <UserCircleIcon class="w-24 h-24 rounded-full shrink-0" />
    <div class="flex flex-col items-start justify-center w-full">
      <h2 class="text-2xl font-bold text-left w-full">{{ user.name }}</h2>
      <p class="text-gray-600 text-left w-full">{{ profile.bio }}</p>
      <div class="flex space-x-4 text-blue-500 mt-2">
        <a :href="profile.linkedin" target="_blank">LinkedIn</a>
        <a :href="profile.github" target="_blank">GitHub</a>
        <a :href="profile.website" target="_blank">Website</a>
      </div>
    </div>
  </div>
</div>


  
      <!-- Skills, Tools, Interests -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-6 p-10">
  <div class="bg-gray-50 p-4 rounded-xl shadow">
    <h4 class="text-lg font-semibold mb-2">Skills</h4>
    <div class="flex flex-wrap gap-2">
      <span v-for="skill in parsed(profile.skills)" :key="skill" class="bg-purple-600 text-white text-sm px-3 py-1 rounded-full">
        {{ skill }}
      </span>
    </div>
  </div>

  <div class="bg-gray-50 p-4 rounded-xl shadow">
    <h4 class="text-lg font-semibold mb-2">Tools</h4>
    <div class="flex flex-wrap gap-2">
      <span v-for="tool in parsed(profile.tools)" :key="tool" class="bg-purple-600 text-white text-sm px-3 py-1 rounded-full">
        {{ tool }}
      </span>
    </div>
  </div>

  <div class="bg-gray-50 p-4 rounded-xl shadow">
    <h4 class="text-lg font-semibold mb-2">Interests</h4>
    <div class="flex flex-wrap gap-2">
      <span v-for="interest in parsed(profile.interests)" :key="interest" class="bg-purple-600 text-white text-sm px-3 py-1 rounded-full">
        {{ interest }}
      </span>
    </div>
  </div>
</div>

  
      <!-- Education Section -->
      <div class="mt-4 px-12" >
        <h3 class="text-xl font-semibold">Education</h3>
        <div v-for="edu in profile.education" :key="edu.id" class="mt-4 flex items-start space-x-4">
            <AcademicCapIcon class="w-12  h-12 text-indigo-600" />
          <div>
            <h4 class="text-md font-bold">{{ edu.degree }}</h4>
            <p class="text-gray-600">{{ edu.institution }}</p>
            <p class="text-sm text-gray-500">{{ formatDate(edu.start_date) }} - {{ edu.current ? 'Present' : formatDate(edu.end_date) }}</p>
          </div>
        </div>
      </div>
  
      <!-- Job Section -->
      <div class="mt-2 px-12">
        <h3 class="text-xl font-semibold">Experience</h3>
        <div v-for="job in profile.jobs" :key="job.id" class="mt-10 flex items-start space-x-4">
            <BuildingOfficeIcon class="w-12  h-12 text-gray-600" />
          <div>
            <h4 class="text-md font-bold">{{ job.position }}</h4>
            <p class="text-gray-600">{{ job.company }} · Full-time</p>
            <p class="text-sm text-gray-500">
              {{ formatDate(job.start_date) }} - {{ job.current_job ? 'Present' : formatDate(job.end_date) }} ·
              {{ jobDuration(job.start_date, job.end_date, job.current_job) }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { AcademicCapIcon } from '@heroicons/vue/24/outline'
    import { BuildingOfficeIcon } from '@heroicons/vue/24/outline'
    import {UserCircleIcon} from '@heroicons/vue/24/solid'
  export default {
    name: 'LinkedInProfileClone',
    components: {
      AcademicCapIcon,
        BuildingOfficeIcon,
        UserCircleIcon
    },
    data() {
      return {
        user: {
          name: 'Jane Doe'
        },
        profile: {
          bio: 'Software engineer with a passion for open source and clean code.',
          linkedin: 'https://www.linkedin.com/in/janedoe',
          github: 'https://github.com/janedoe',
          website: 'https://janedoe.dev',
          skills: 'JavaScript, Vue.js, Python',
          tools: 'VS Code, Git, Docker',
          interests: 'Open Source, AI, Teaching',
          education: [
            {
              id: 1,
              institution: 'MIT',
              degree: 'B.Sc. Computer Science',
              start_date: '2015-08-01',
              end_date: '2019-05-31',
              current: false
            }
          ],
          jobs: [
            {
              id: 1,
              company: 'TechCorp',
              position: 'Frontend Developer',
              start_date: '2019-06-01',
              end_date: '2022-12-31',
              current_job: false
            },
            {
              id: 2,
              company: 'InnovateX',
              position: 'Senior Developer',
              start_date: '2023-01-01',
              end_date: null,
              current_job: true
            }
          ]
        }
      };
    },
    methods: {
      parsed(str) {
        return str ? str.split(',').map(s => s.trim()) : [];
      },
      formatDate(dateStr) {
        if (!dateStr) return '';
        const options = { year: 'numeric', month: 'short' };
        return new Date(dateStr).toLocaleDateString(undefined, options);
      },
      jobDuration(start, end, isCurrent) {
        const startDate = new Date(start);
        const endDate = isCurrent ? new Date() : new Date(end);
        const months = (endDate.getFullYear() - startDate.getFullYear()) * 12 + (endDate.getMonth() - startDate.getMonth());
        const years = Math.floor(months / 12);
        const remMonths = months % 12;
        return `${years ? years + ' yr' + (years > 1 ? 's' : '') : ''}${years && remMonths ? ' ' : ''}${remMonths ? remMonths + ' mo' + (remMonths > 1 ? 's' : '') : ''}`.trim();
      }
    },
    mounted: async function () {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/user-profile', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authentication-Token': `${localStorage.getItem('authtoken')}`
      }
    });
    if (response.status === 401) {
    console.error('Unauthorized access. Please log in.');
    this.$router.push('/signin');
    return;
  }
    if (!response.ok) {
      throw new Error('Failed to fetch profile data');
    }

    const data = await response.json();
    this.user.name = data.name;
    this.profile = data.profile;
    console.log("Profile data:", this.profile);
  } catch (error) {
    console.error('Error loading profile:', error);
  }
}

  };
  
  </script>
  
  <style scoped>
  </style>