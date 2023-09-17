<template>
    <div class="container">
            <div class="items">
                <ul class="column">
                    <li><input type="file" ref="file" @change="handleFileUpload()" placeholder="File"></li>
                    <li><button @click="onPush">Push</button></li>
                    <li><button @click="this.$router.push(`/user/${this.user_id}/home`,{user_id:this.user_id})">Домашняя страница</button></li>
                </ul>
            </div>
        </div>
</template>
    
<script>
import axios from 'axios'
export default {
    data() {
        return {
            file: '',
            api_url:'',
            user_id: 0
        }
    },
    methods: {
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        },
        async onPush() {
            this.api_url = `http://localhost:8000/user/${this.user_id}/upload/`;
            const formData = new FormData();
                formData.append('file',this.file);
                try {
                  const response = await axios.post(
                    this.api_url,
                      formData, {
                        headers: {
                          'Content-Type': 'multipart/form-data'
                        },
                      });
                  console.log(response.data);
                } catch(error) {
                  console.log(error);
                }
        }
    },
    mounted() {
        this.user_id = this.$route.params.user_id;
    }
}
</script>
    
<style scoped>
@import url("/public/styles/column.css");
</style>