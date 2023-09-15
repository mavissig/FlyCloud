<template>
    <div id="main_page">
            <ul class="title">
                <li><img class="cloud_title_image"></li>
                <li><p class="text_style">FlyCloud</p></li>
                <li><BinderLine></BinderLine></li>
                <li><TitleButton @click="page_index=0">О нас</TitleButton></li>
                <li><BinderLine></BinderLine></li>
                <li><TitleButton @click="page_index=1">Контакты</TitleButton></li>
                <li><BinderLine></BinderLine></li>
                <li><TitleButton @click="page_index=2">Личный кабинет</TitleButton></li>
            </ul>
            <Line></Line>
            <div v-if="page_index==0">
                <MainPageContent></MainPageContent>
            </div>
            <div v-else-if="page_index==1">
            </div>
            <div v-else-if="page_index==2">
                <Auth></Auth>
            </div>
            <Line></Line>
    </div>
</template>

<script>
import BinderLine from "@/components/BinderLine.vue"
import TitleButton from "@/components/TitleButton.vue"
import Line from "@/components/Line.vue"
import MainPageContent from "@/components/MainPageContent.vue"
import Auth from "@/components/Auth.vue"

export default {
    components: {
        BinderLine,
        TitleButton,
        Line,
        MainPageContent,
        Auth
    },
    data() {
        return {
            page_index:0
        }
    }
}
</script>

<style>
@import url("../public/styles/TextStyle.css");
html {
  margin: 0;
  padding: 0;
  border: 0;
  background-color:#E2DCDC;;
  font-size: 100%;
  flex-shrink: 0;
  font: inherit;
  vertical-align: baseline;
  outline: none;
}


.title {
    text-align: center;
    padding: 0;
    margin-left: auto;
}

.title li {
    white-space: nowrap;
    margin-left: 5px;
    display: inline-block;
}

.cloud_title_image {
    background: url("/images/cloud_title.png");
    background-repeat: no-repeat;
    width: 78px;
    height: 76px;
    flex-shrink: 0;
}


</style>