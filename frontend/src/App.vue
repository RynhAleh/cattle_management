<template>
  <div id="app">
    <!-- Отображаем компоненты в зависимости от маршрута -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  display: flex;
}
</style>