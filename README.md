# 🧠 Review Sentiment Service

Сервис для сбора и анализа отзывов пользователей в реальном времени.  
Определяет настроение отзыва (positive, negative, neutral) и сохраняет в SQLite.  
Создан на базе **FastAPI**, с продвинутой структурой и Docker-развёрткой.

---

## 🚀 Быстрый старт

### 1. Клонируй проект

```bash
git clone https://github.com/Albert-Sadykov/Review_sentiment_service.git
cd review-sentiment-service
```

# Убедись, что установлен Docker

```bash
docker --version
docker-compose --version
```

# Запусти проект

```bash
docker-compose up --build
```

# 🧪 Тестирование API
<p>Swagger UI 👉 http://localhost:8000/docs</p>
<p>ReDoc 👉 http://localhost:8000/redoc</p>

## 📬 Примеры запросов

### ➕ Добавить отзыв (POST)

```bash
curl -X POST http://localhost:8000/reviews \
     -H "Content-Type: application/json" \
     -d '{"text": "Обожаю этот продукт!"}'
```

### Пример ответа

```json
{
  "id": 1,
  "text": "Обожаю этот продукт!",
  "sentiment": "positive",
  "created_at": "2025-07-25T14:12:00.123456+00:00"
}
```

### 📋 Получить все отзывы (GET)

```bash
curl http://localhost:8000/reviews
```

### Пример ответа:

```json
[
  {
    "id": 1,
    "text": "Обожаю этот продукт!",
    "sentiment": "positive",
    "created_at": "2025-07-25T14:12:00.123456+00:00"
  },
  {
    "id": 2,
    "text": "Плохо работает сервис",
    "sentiment": "negative",
    "created_at": "2025-07-25T14:15:00.654321+00:00"
  }
]
```

### 📉 Получить только негативные отзывы (GET)

```bash
curl "http://localhost:8000/reviews?sentiment=negative"
```

### Пример ответа:

```json
[
  {
    "id": 2,
    "text": "Плохо работает сервис",
    "sentiment": "negative",
    "created_at": "2025-07-25T14:15:00.654321+00:00"
  }
]
```