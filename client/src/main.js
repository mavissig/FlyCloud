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
        {path: '/home/user/:id',name:'User',component:User},
        {path: '/home/user/:id/upload',name:'Upload',component:Upload},
        {path: '/home/user/:id/files',name:'Files',component:Files},
        {path: '/home/user/:id/files/file_content//:content_id',name:'FileContent',component:FileContent}
    ]
});

createApp(App).use(router).mount('#app');