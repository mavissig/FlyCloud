<template>
    <div class="container">
        <div class="items">
            <button v-if="show_auth==false" @click="show_auth=true">Auth</button>
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
body {
    margin: 0;
    padding: 0;
    background:#E2DCDC;
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