<template>
  <div class="login-container">
    <h2>Вход в систему</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Имя пользователя:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Пароль:</label>
        <input type="password" v-model="password" id="password" required autocomplete="current-password"/>
      </div>
      <button type="submit">Войти</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      users: [],
      errorMessage: '',
    };
  },
  methods: {
    async fetchUsers() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('/api/users/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.users = response.data; // Обработка ответа с пользователями
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async handleLogin() {
      try {
        const response = await axios.post('/api/token/', {
          username: this.username,
          password: this.password,
        });
        // Сохраните токен в localStorage
        localStorage.setItem('token', response.data.access); // Изменили на access
        // Теперь, после успешного входа, получаем пользователей
        await this.fetchUsers(); // Запрашиваем пользователей после логина
        // Перенаправляем на Dashboard
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Вход не осуществлен:', error);
        this.errorMessage = 'Неверное имя пользователя или пароль'; // Сообщение об ошибке
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.login-container:hover {
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

h2 {
  text-align: center;
  color: #333;
  font-family: 'Arial', sans-serif;
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-color: #007BFF;
  outline: none;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>
