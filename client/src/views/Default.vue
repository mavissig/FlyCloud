<template>
    <div class="center">
        <div>
            <button  class="glow-on-hover" v-if="show_auth==false" @click="show_auth=true">Auth</button>
            <Auth v-else @onBack='Show'></Auth>
        </div>
    </div>
</template>

<script>
import Auth from './../components/default/Auth.vue'

export default {
    components: {
        Auth
    },
    data() {
        return {
            show_auth: false
        }
    },
    methods: {
        Show() {
            this.show_auth = false;
        }
    }
}
</script>

<style>
@import url("/public/styles/column.css");
@import url("/public/styles/button_rgb.css");
@import url("/public/styles/center.css");


html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background: #000;
}

</style>