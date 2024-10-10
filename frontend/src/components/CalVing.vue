<template>
  <div>
    <div style="margin-bottom: 16px">
      <a-button type="primary" :disabled="!hasSelected" :loading="state.loading" @click="fetchData">
        Reload
      </a-button>
      <span style="margin-left: 8px">
        <template v-if="hasSelected">
          {{ `Selected ${state.selectedRowKeys.length} items` }}
        </template>
      </span>
    </div>
    <a-table
      :row-selection="{ selectedRowKeys: state.selectedRowKeys, onChange: onSelectChange }"
      :columns="columns"
      :data-source="state.data"
      :loading="state.loading"
    />
  </div>
</template>

<script setup>
import { computed, reactive, onMounted } from 'vue';
import axios from 'axios'; // используем axios для выполнения HTTP запросов

const columns = [
  {
    title: 'ID',
    dataIndex: 'id',
  },

  {
    title: 'Name',
    dataIndex: 'name',
  },
  {
    title: 'Color',
    dataIndex: 'color',
  },
  {
    title: 'Birth',
    dataIndex: 'birth',
  },
  {
    title: 'Weight',
    dataIndex: 'weight',
  },
];

const state = reactive({
  selectedRowKeys: [],
  data: [], // данные из API
  loading: false,
});

const hasSelected = computed(() => state.selectedRowKeys.length > 0);

// Функция для получения данных из API
const fetchData = async () => {
  state.loading = true;
  try {
    const response = await axios.get('http://0.0.0.0:8000/api/cattle/'); // Замените на URL вашего API
    state.data = response.data; // Предполагается, что данные будут в формате массива
  } catch (error) {
    console.error('Ошибка при получении данных:', error);
  } finally {
    state.loading = false;
  }
};

const onSelectChange = selectedRowKeys => {
  console.log('selectedRowKeys changed: ', selectedRowKeys);
  state.selectedRowKeys = selectedRowKeys;
};

// Автоматическая загрузка данных при монтировании компонента
onMounted(() => {
  fetchData();
});
</script>
