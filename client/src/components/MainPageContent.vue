<template>
    <div id="main_page_content" class="main_page_content">
        <div id="top_content" class="top_content">
            <ul>
            <li id="top_text_content">
                <BlackBox>
                    <div class="inner_content">
                        <div class="inner_text_content">
                            FlyCloud - ваш персональный помощник для работы<br>
                            с файлами. В нем вы можете редактировать их,<br>
                            хранить, выгружать, удалять и многое другое!
                        </div>
                        <TitleButton style=" align-self: flex-end;">Хочу попробовать!</TitleButton>
                    </div>
                </BlackBox>
            </li>
                <li><img src="/images/image_content_1.png" class="image_content"></li>
            </ul>
        </div>
        <div id="down_content" class="down_content">
            <ul>
                <li><img src="/images/image_content_2.png" class="image_content"></li>
            <li id="down_text_content">
                <BlackBox>
                    <div class="inner_content">
                        <div class="inner_text_content">
                            FlyCloud - это...<br>
                            <ul>
                                <li>надежность</li><br>
                                <li>многогогранность</li><br>
                                <li>доступность</li>
                            </ul>
                        </div>
                    </div>
                </BlackBox>
            </li>
            </ul>
        </div>
    </div>
</template>

<script>
import TitleButton from "@/components/TitleButton.vue"
import BlackBox from "@/components/BlackBox.vue"

export default {
    components: {
        TitleButton,
        BlackBox
    }
}
</script>

<style>
.main_page_content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.top_content {
    margin-top: 219px;
    margin-left: 49px;
}

.top_content li {
    white-space: nowrap;
    display: inline-block;
}

.inner_content {
    position: absolute;
    flex-direction: column;
    display: flex;
}

.down_content {
    margin-left: 49px;
    margin-top: 70px;
}

.down_content li {
    white-space: nowrap;
    display: inline-block;
}

.inner_text_content {
    padding-left: 22px;
    padding-top: 38px;
    width: 332px;
    height: 140px;
    flex-shrink: 0;
    color: #FFF;
    font-family: Raleway;
    font-size: 14px;
    font-style: normal;
    font-weight: 600;
    line-height: 17px;
}


.image_content {
    width: 366px;
    height: 239px;
    flex-shrink: 0;
    background:  lightgray 50% / cover no-repeat;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    background-repeat: no-repeat;
}

</style>