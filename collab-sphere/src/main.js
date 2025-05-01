import { createApp } from 'vue'
import App from './App.vue'
import './assets/tailwind.css'
import router from './router'
import store from "./store.js"

const app = createApp(App)

app.use(router)
app.use(store)
app.mount('#app')

const globaldata = {
    backendUrl: "http://localhost:5000",
}
app.config.globalProperties.$globaldata =globaldata