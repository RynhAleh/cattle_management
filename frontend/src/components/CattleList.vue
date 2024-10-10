<template>
  <div>
    <h1>Список животных</h1>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Имя</th>
            <th>Окрас</th>
            <th>Дата рождения</th>
            <th>Вес при рождении</th>          
            <!-- Добавьте дополнительные заголовки для всех полей -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="animal in cattle" :key="animal.id">
            <td>{{ animal.id }}</td>
            <td>{{ animal.name }}</td>
            <td>{{ animal.color }}</td>
            <td>{{ animal.birth }}</td>
            <td>{{ animal.weight }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <h2>Добавить животное</h2>
    <form @submit.prevent="addCattle">
      <label for="f01">Кличка:</label>
      <input id="f01" type="text" v-model="newCattle.name" required />
      
      <label for="f02">Окрас:</label>
      <input id="f02" type="text" v-model="newCattle.color" required />
      
      <label for="f03">Дата рождения:</label>
      <input id="f03" type="date" v-model="newCattle.birth" required />

      <label for="f04">Вес при рождении:</label>
      <input id="f04" type="number" v-model="newCattle.weight" required />

      <button type="submit">Добавить</button>
    </form>

  </div>
</template>

<script>
export default {
  data() {
    return {
      cattle: [], // Список животных
      newCattle: {
        name: '',
        color: '',
        birth: '',
        weight: ''
      }      
    };
  },
  created() {
    this.fetchCattle(); // Запрос данных при создании компонента
  },
  methods: {
    async fetchCattle() {
      try {
        const response = await fetch('http://0.0.0.0:8000/api/cattle/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        this.cattle = await response.json(); // Запись данных в cattle
      } catch (error) {
        console.error('Ошибка при получении данных:', error);
      }
    },
    async addCattle() {
      try {
        const response = await fetch('http://0.0.0.0:8000/api/cattle/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newCattle),
        });

        if (response.ok) {
          const addedCattle = await response.json();
          this.cattle.push(addedCattle); // Добавляем нового животного в список
          this.newCattle.name = ''; // Очищаем поля формы
          this.newCattle.color = '';
          this.newCattle.birth = '';
          this.newCattle.weight = '';
        } else {
          console.error('Ошибка при добавлении животного:', response.statusText);
        }
      } catch (error) {
        console.error('Ошибка при отправке данных:', error);
      }
    },
  },
};
</script>

<style scoped>
.table-container {
  width: calc(100% - 0px); /* Замените 250px на фактическую ширину боковой панели */
  height: calc(100vh - 350px); /* Высота страницы минус форма ввода (например, 150px) */
  overflow-y: auto;
  border: 1px solid #ddd;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table th {
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #e2ffe2; /* Бледно-зелёный цвет для шапки таблицы */
  color: #000; /* Цвет текста в шапке */
}

table td {
  padding: 10px;
  border: 1px solid #ccc;
}
</style>