<template>
  <div id="app">
    <SideBar @section-selected="updateCurrentSection" />
    <div class="content">
      <component :is="currentSection"></component>
    </div>
  </div>
</template>

<script>
import SideBar from './SideBar.vue';
import CattleList from './CattleList.vue';
import CalVing from './CalVing.vue';
import Feeding from './FeeDing.vue';


export default {
  components: {
    SideBar,
    CattleList,
    CalVing,
    Feeding,
  },
  data() {
    return {
      currentSection: 'CattleList', // По умолчанию отображаем CattleList
    };
  },
  methods: {
    updateCurrentSection(section) {
      switch (section) {
        case 'cattleList':
          this.currentSection = 'CattleList';
          break;
        // Здесь можно добавить дополнительные случаи для других разделов
        case 'insemination':
          this.currentSection = 'Insemination'; // предположим, вы создадите этот компонент
          break;
        case 'feeding':
          this.currentSection = 'Feeding'; // предположим, вы создадите этот компонент
          break;
        case 'milking':
          this.currentSection = 'Milking'; // предположим, вы создадите этот компонент
          break;
        case 'movement':
          this.currentSection = 'Movement'; // предположим, вы создадите этот компонент
          break;
        case 'arrival':
          this.currentSection = 'CalVing'; // предположим, вы создадите этот компонент
          break;
        case 'treatment':
          this.currentSection = 'Treatment'; // предположим, вы создадите этот компонент
          break;
        case 'culling':
          this.currentSection = 'Culling'; // предположим, вы создадите этот компонент
          break;
        default:
          this.currentSection = 'CattleList';
      }
    }
  }
};
</script>

<style>
#app {
  display: flex;
}
.content {
  flex: 1;
  padding: 20px;
}
</style>