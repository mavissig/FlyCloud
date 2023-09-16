<template>
    <div class="container">
        <div class="items">
            <button v-if="show_auth==false" @click="show_auth=true">Auth</button>
            <div v-else>
                <ul class="auth">
                    <li><input @input="username = $event.target.value" type="input" placeholder="Login"></li>
                    <li><input @input="password = $event.target.value" type="input" placeholder="Password"></li>
                    <li><button @click="onLog">Log</button></li>
                    <li><button @click="onReg">Registry</button></li>
                    <li><button @click="show_auth=false">Back</button></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            show_auth: false,
            username: "",
            password: ""
        }
    },
    methods: {
        async onLog() {
            await axios({
                method: 'post',
                url: 'http://localhost:8000/auth/',
                timeout: 5000,
                data: {
                    username : this.username,
                    password: this.password
                }
            }).then(response => {
                alert('Yes'); console.log(response.data); this.$router.push('home/user/1/upload');
            }).catch(error => { console.log(error); alert('Ошибка входа');});
        },
        onReg() {
            this.$router.push('/registration');
        }
    }
}
</script>

<style>
body {
    margin: 0;
    padding: 0;
    background:#E2DCDC;
}



.auth  li {
    list-style-type: none;
}

.container {
    display: flex;
    flex-direction: column;
    text-align: center;
}

.items {
    position: absolute;
    top: 50%;
    left: 50%;
}

</style>