<template>
    <div @keypress.enter="onLog">
        <ul class="column">
            <li><input @input="username = $event.target.value" type="input" placeholder="Login"></li>
            <li><input @input="password = $event.target.value" type="input" placeholder="Password"></li>
            <li><button @click="onLog">Войти</button></li>
            <li><button @click="this.$router.push('/registration')">Регистрация</button></li>
            <li><button @click="this.$emit('onBack')">Назад</button></li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            username: '',
            password: '',
            api_url: 'http://localhost:8000/auth/',
            auth_timout:5000,
            info: null
        }
    },
    methods: {
        async onLog() {
            await axios({
                method: 'post',
                url: this.api_url,
                timeout: this.auth_timout,
                data: {
                    username: this.username,
                    password: this.password
                }
            }).then(response => {this.info = response.data;
                                 this.$router.push(`/user/${this.info.user_id}/home`,{user_id:this.info.user_id});});
        }
    }
}
</script>


<style scoped>

</style>