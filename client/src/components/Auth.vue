<template>
    <div @keyup.enter="send_to_api">
        <BlackBox>
            <div>
                <p class="text_style" style="color: white; font-size: 30px;">Авторизация</p>
                <label></label>
                <input @input="username = $event.target.value" id="login" placeholder="Login">
                <label></label>
                <input @input="password = $event.target.value" id="password" placeholder="Password">
                <TitleButton @click="send_to_api">Auth</TitleButton>
            </div>
        </BlackBox>
    </div>
</template>

<script>
import BlackBox from "@/components/BlackBox.vue"
import TitleButton from "@/components/TitleButton.vue"
import axios from 'axios'

export default {
    components: {
        BlackBox,
        TitleButton
    },
    data() {
        return {
            username: "",
            password: "",
            info: null,
            api_url: 'http://localhost:8000/auth/',
            timeout: 5000
        }
    },
    methods: {
        async send_to_api(){
            await axios({
                method: 'post',
                url: this.api_url,
                timeout: this.timeout,
                data: {
                    username: this.username,
                    password: this.password
                }
            }).then(response => { this.info = response.data; console.log(this.info); alert('Получилось! смотри логи!') })
                .catch(error => { console.log(error); alert('Не получилось получить данные! смотри логи!') })
        }
    }
}
</script>

<style scoped>
div {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
    margin-bottom: 30px;
}
</style>