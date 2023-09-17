<template>
<div @keyup.enter="onReg" class="form__group field">
    <ul>
        <li><input v-model="email" type="input" class="form__field" placeholder="Email" name="email" id='email'></li>
        <li><input v-model="username" type="input" class="form__field" placeholder="Login" name="login" id='login'></li>
        <li><input v-model="password" type="input" class="form__field" placeholder="Password" name="password" id='password'></li>
        <li><input v-model="password_check" type="input" class="form__field" placeholder="CheckPassword" name="check_password" id='check_password'></li>
        <li><button @click="onReg" class="glow-on-hover">Registration</button></li>
        <li><button class="glow-on-hover" @click="this.$router.push('/')">Back</button></li>
    </ul>
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
            password_check: "",
            api_url :'http://localhost:8000/auth/reg/'
        }
    },
    methods: {
        async onReg() {
            await axios({
                method: 'post',
                url: this.api_url,
                timeout: 5000,
                data: {
                    email: this.email,
                    username : this.username,
                    password: this.password,
                    password_check : this.password_check
                }
            }).then(_ => {
                this.$router.push('/');
            }).catch(error => { console.log(error);});
        }
    }
}
</script>

<style scoped>

li {
    list-style-type: none;
    margin-top: 30px;
}

button {
    margin-top: 15px;
}

.form__group {
	 position: relative;
	 padding: 15px 0 0;
	 margin-top: 10px;
	 width: 50%;
}
 .form__field {
	 font-family: inherit;
	 width: 100%;
	 border: 0;
	 border-bottom: 2px solid #9b9b9b;
	 outline: 0;
	 font-size: 1.3rem;
	 color: #fff;
	 padding: 7px 0;
	 background: transparent;
	 transition: border-color 0.2s;
}
 .form__field::placeholder {
	 color: transparent;
}
 .form__field:placeholder-shown ~ .form__label {
	 font-size: 1.3rem;
	 cursor: text;
}
 .form__label {
	 top: 500;
	 display: block;
	 transition: 0.2s;
	 font-size: 1rem;
	 color: #9b9b9b;
}
 .form__field:focus {
	 padding-bottom: 6px;
	 font-weight: 700;
	 border-width: 3px;
	 border-image: linear-gradient(to right, #11998e, #38ef7d);
	 border-image-slice: 1;
}
 .form__field:focus ~ .form__label {
	 position: absolute;
	 top: 0;
	 display: block;
	 transition: 0.2s;
	 font-size: 1rem;
	 color: #11998e;
	 font-weight: 700;
}
/* reset input */
 .form__field:required, .form__field:invalid {
	 box-shadow: none;
}

</style>