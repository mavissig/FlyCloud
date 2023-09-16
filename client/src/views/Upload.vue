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
import axios from 'axios'
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
              await axios({
                method:'post',
                url: 'http://localhost:8000/user/upload/',
                data: {
                  file: 'api'
                }
              }).then(response => {alert('Yes');}).catch(error => {alert('No');});
                // const formData = new FormData();
                // formData.append('file',this.file);
                // try {
                //   const response = await axios.post(
                //       'http://localhost:8000/user/upload/',
                //       formData, {
                //         headers: {
                //           'Content-Type': 'multipart/form-data'
                //         },
                //       });
                //   console.log(response.data);
                // } catch(error) {
                //   console.log(error);
                // }
            }
        }
    }
    </script>
    
    <style scoped>
    
    </style>