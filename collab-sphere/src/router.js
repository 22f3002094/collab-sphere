import {createRouter, createWebHistory} from 'vue-router'
import WelCome from './pages/WelCome.vue'

const routes = [
    {
        path:"/",
        name: "WelCome",
        component: WelCome
    },
    {
        path:"/signup",
        name: "SignUp",
        component: () => import('./pages/SignUp.vue')
    },
    {
        path:"/signin",
        name: "SignIn",
        component: () => import('./pages/SignIn.vue')
    },
    {
        path:"/home",
        name: "Home",     
        component: () => import('./pages/Home.vue')
    },
    {
        path:"/newproject",
        name: "NewProject",
        component: () => import('./pages/NewProject.vue')
    },
    {
        path:"/myprojects",
        name: "MyProjects",
        component: () => import('./pages/MyProjects.vue')
    },
    {
        path:"/project/:slug",
        name: "Project",
        component: () => import('./pages/ProjectPage.vue')
    },
    {
        path:"/askai",
        name: "AskAI",
        component: () => import('./pages/AskAI.vue')
    },
    {
        path:"/@:username",
        name: "Profile",
        component: () => import('./components/Dummy.vue')
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router