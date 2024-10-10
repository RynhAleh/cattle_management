# Используем официальный образ Node.js 18
FROM node:18-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package.json package-lock.json ./

# Устанавливаем зависимости
RUN npm install --silent

# Копируем все файлы проекта, кроме node_modules (исключается через .dockerignore)
COPY . .

# Открываем порт 8080 для Vue приложения
EXPOSE 8080

# Команда для запуска Vue dev сервера
CMD ["npm", "run", "serve", "--", "--host", "0.0.0.0", "--port", "8080"]