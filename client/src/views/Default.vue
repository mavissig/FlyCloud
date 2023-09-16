<template>
    <div>
        <ul class="default_title">
            <li><img class="title_cloud"></li>
            <li class="title_text">FlyCloud</li>
            <li><button>123</button></li>
            <li><button>123</button></li>
            <li><button>123</button></li>
        </ul>
    </div>
</template>

<script>
export default {

}
</script>

<style>
body {
    margin: 0;
    padding: 0;
    background:#E2DCDC;
}

.default_title {
    white-space: nowrap;
}

.default_title li {
    display: inline-block;
    margin-left: 12px;
}

.title_text {
    width: 151px;
    height: 43px;
    flex-shrink: 0;
    color: #000;
    font-family: Raleway;
    font-size: 35px;
    font-style: normal;
    font-weight: 600;
    line-height: normal;
}

.title_cloud {
    margin-bottom: -15px;
    fill-opacity:inherit;
    width: 78px;
    height: 76px;
    flex-shrink: 0;
    background: url('/public/title_cloud.svg');
    background-repeat: no-repeat;
    background-color: lightgray 50%;
}

</style>