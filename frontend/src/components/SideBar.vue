<template>
  <div class="sidebar">
    <h2>Боковая панель</h2>
    <ul>
      <li @click="selectSection('cattleList')">Журнал животных</li>
      <li @click="selectSection('insemination')">Осеменение</li>
      <li @click="selectSection('feeding')">Кормление</li>
      <li @click="selectSection('milking')">Дойка</li>
      <li @click="selectSection('movement')">Перемещение</li>
      <li @click="selectSection('arrival')">Приход</li>
      <li @click="selectSection('treatment')">Лечение</li>
      <li @click="selectSection('culling')">Выбытие</li>
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    selectSection(section) {
      this.$emit('section-selected', section);
    }
  }
};
</script>

<style>
.sidebar {
  width: 200px;
  background-color: #f4f4f4;
  padding: 20px;
}
.sidebar ul {
  list-style-type: none;
  padding: 0;
}
.sidebar li {
  cursor: pointer;
  margin: 10px 0;
}
.sidebar li:hover {
  text-decoration: underline;
}
</style>