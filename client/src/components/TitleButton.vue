<template>
    <button class="title_button"><slot></slot></button>
</template>

<script>

</script>

<style>

.title_button {
    width: 135px;
    height: 30px;
    flex-shrink: 0;
    background-color: #057D9F;
    border: none;
    border-radius: 15px;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
}

.title_button:hover {
    width: 136px;
    height: 31px;
    background-color: #61B7CF;
}

</style>