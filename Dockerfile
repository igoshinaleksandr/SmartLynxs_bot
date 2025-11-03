# 1. Базовый образ с Python
FROM python:3.10.11

# 2. Рабочая директория
WORKDIR /app

# 3. Копируем зависимости
COPY requirements.txt .

# 4. Устанавливаем зависимости (внутри контейнера)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем остальной код
COPY . .

# 6. Определяем команду запуска
CMD ["python", "main.py"]