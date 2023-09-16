<template>
    <div class="container">
            <div class="items">
                <ul class="auth">
                    <li><input type="file" ref="file" @change="handleFileUpload()" placeholder="File"></li>
                    <li><button @click="onPush">Push</button></li>
                    <li><button ><router-link to="/">exit</router-link></button></li>
                    <li><button ><router-link to="/user/1/home">home</router-link></button></li>
                </ul>
            </div>
        </div>
</template>
    
<script>
    export default {
        data() {
            return {
                file: ''
            }
        },
        methods: {
            handleFileUpload() {
                this.file = this.$refs.file.files[0];
            },
            async onPush() {
                let formData = new FormData();
                formData.append('file',this.file);
                formData.append('name',this.file.name);
                await axis({
                    method: 'post',
                    url: 'http://localhost:8000/upload/',
                    timeout: 5000,
                    data: {
                        FormData: formData
                    },
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                   
                }).catch(error => { console.log(error);});
            }
        }
    }
    </script>
    
    <style scoped>
    
    </style>