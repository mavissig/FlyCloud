import { createApp } from 'vue'

import {createRouter, createWebHistory} from 'vue-router'

import App from './App.vue'
import Default from './views/Default.vue'
import Registration from './views/Registration.vue'

import Files from './views/Files.vue'
import Home from './views/Home.vue'
import Upload from './views/Upload.vue'
import User from './views/User.vue'
import FileContent from './views/FileContent.vue'

const router = createRouter({
    history: createWebHistory(),
    routes:[
        {path:'/',name:'Default',component:Default},
        {path:'/registration',name:'Registration',component:Registration},
        {path: '/home', name:'Home',component:Home},
        {path: '/home/user-*',name:'User',component:User},
        {path: '/home/user-*/upload',name:'Upload',component:Upload},
        {path: '/home/user-*/files',name:'Files',component:Files},
        {path: '/home/user-*/files/file_content-*',name:'FileContent',component:FileContent}
    ]
});

createApp(App).use(router).mount('#app');