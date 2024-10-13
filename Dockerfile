# Базовый образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install --no-cache-dir opencv-python-headless

# Копируем все файлы проекта в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Команда для запуска приложения
CMD ["python", "app.py"]