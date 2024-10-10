# Используем официальный образ Python 3.11
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все исходные файлы приложения
COPY . .

# Открываем порт 8000 для приложения
EXPOSE 8000

# Команда для запуска приложения через Django runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]