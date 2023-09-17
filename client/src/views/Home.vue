<template>
    <div class="container">
            <div class="items">
                <ul class="column">
                    <li><button @click="this.$router.push(`/user/${this.user_id}/files`)">Files</button></li>
                    <li><button @click="this.$router.push(`/user/${this.user_id}`)">User</button></li>
                    <li><button @click="this.$router.push(`/user/${this.user_id}/upload`,{user_id:this.user_id})">Upload</button></li>
                    <li><button><router-link to="/">exit</router-link></button></li>
                </ul>
            </div>
        </div>
</template>
    
<script>
export default {
    data() {
        return {
            user_id: 0
        }
    },
    mounted() {
        this.user_id = this.$route.params.user_id;
    }
}
</script>
    
<style scoped>
@import url("./../../public/styles/column.css");
</style>