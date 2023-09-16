<template>
    <div class="container">
            <div class="items">
                <ul class="column">
                    <li><button><router-link to="/user/{{this.$route.params.user_id }}/files">Files</router-link></button></li>
                    <li><button ><router-link to="/user/{{this.$route.params.user_id}}">User</router-link></button></li>
                    <li><button ><router-link to="/user/{{this.$route.params.user_id}}/upload">Upload</router-link></button></li>
                    <li><button ><router-link to="/">exit</router-link></button></li>
                </ul>
            </div>
        </div>
</template>
    
<script>
export default {
}
</script>
    
<style scoped>
@import url("./../../public/styles/column.css");
</style>