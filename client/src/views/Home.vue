<template>
    <div class="center">
            <div>
                <ul class="column">
                    <li><button class="glow-on-hover" @click="this.$router.push(`/user/${this.user_id}/files`)">Files</button></li>
                    <li><button class="glow-on-hover" @click="this.$router.push(`/user/${this.user_id}`)">User</button></li>
                    <li><button class="glow-on-hover" @click="this.$router.push(`/user/${this.user_id}/upload`,{user_id:this.user_id})">Upload</button></li>
                    <li><button class="glow-on-hover" @click="this.$router.push('/')">Exit</button></li>
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