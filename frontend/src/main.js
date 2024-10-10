import { createApp } from 'vue';
import App from './App.vue';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css';
import router from './router';

const app = createApp(App);

app.use(Antd);  // Используем Ant Design Vue как плагин
app.use(router);
app.mount('#app');