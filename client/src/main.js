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
        {path: '/user/:id/home', name:'Home',component:Home},
        {path: '/user/:id',name:'User',component:User},
        {path: '/user/:id/upload',name:'Upload',component:Upload},
        {path: '/user/:id/home/files',name:'Files',component:Files},
        {path: '/user/:id/home/files/file_content//:content_id',name:'FileContent',component:FileContent}
    ]
});

createApp(App).use(router).mount('#app');