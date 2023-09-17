<template>
<div @keypress.enter="onReg" class="container">
        <div class="items">
            <ul class="column">
                <li><input @input="email = $event.target.value" type="input" placeholder="Почта"></li>
                <li><input @input="username = $event.target.value" type="input" placeholder="Логин"></li>
                <li><input @input="password = $event.target.value" type="input" placeholder="Пароль"></li>
                <li><input @input="password_check = $event.target.value" type="input" placeholder="Повторите пароль"></li>
                <li><button @click="onReg">Registry</button></li>
                <li><button ><router-link to="/">Back</router-link></button></li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            email: "",
            username: "",
            password: "",
            password_check: ""
        }
    },
    methods: {
        async onReg() {
            await axios({
                method: 'post',
                url: 'http://localhost:8000/auth/reg/',
                timeout: 5000,
                data: {
                    email: this.email,
                    username : this.username,
                    password: this.password,
                    password_check : this.password_check
                }
            }).then(response => {
                this.$router.push('/');
            }).catch(error => { console.log(error);});
        }
    }
}
</script>

<style scoped>
@import url("./../../public/styles/column.css");
</style>