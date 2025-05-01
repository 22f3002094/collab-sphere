<template>
    <div>
     <OnboardingCard v-if="showOnboarding" /> 
      <Feed v-else />
    </div>
  </template>
  
  <script>
  import Feed from "@/components/Feed.vue";
  import OnboardingCard from "@/components/OnBoarding.vue";
  export default {
    name: "HomePage",
    // setup() {
    //   const showOnboarding = this.$route.query.onboard === "true";
    //   return { showOnboarding };
    // }
    components: {
      Feed,
        OnboardingCard,
    },
    mounted(){
        if(localStorage.getItem("authtoken")){
            console.log("Token exists")
        } else {
            this.$router.push("/signin")
        }
    },
    computed: {
      showOnboarding() {
        return this.$route.query.onboard === "true";
      }
    },
  }
  </script>
  