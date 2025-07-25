FROM python:3.11-slim

WORKDIR /app

# Установка uv
RUN pip install uv

# Копируем проект
COPY . .

# Установка зависимостей в системное окружение
RUN uv pip install --system -r requirements.uv

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
