<template>
<div class="container">
        <div class="items">
            <ul class="auth">
                <li><input @input="username = $event.target.value" type="input" placeholder="Login"></li>
                <li><input @input="password = $event.target.value" type="input" placeholder="Password"></li>
                <li><button @click="onReg">Registry</button></li>
                <li><button ><router-link to="/">Back</router-link></button></li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        async onReg() {
            await axis({
                method: 'post',
                url: 'http://localhost:8000/reg/',
                timeout: 5000,
                data: {
                    username : this.username,
                    password: this.password
                }
            }).then(response => {
                this.$router.push('/');
            }).catch(error => { console.log(error); alert('Ошибка регистрации');});
        }
    }
}
</script>

<style scoped>

</style>