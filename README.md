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
<a href='http://localhost:8000/docs' style='color: #000; text-decoration: none;'>Swagger UI</a> 👉 http://localhost:8000/docs
<a href='http://localhost:8000/redoc' style='color: #000; text-decoration: none;'>ReDoc</a> 👉 http://localhost:8000/redoc

# 📬 Примеры запросов
POST запрос
```bash
curl -X POST http://localhost:8000/reviews \
     -H "Content-Type: application/json" \
     -d '{"text": "Обожаю этот продукт!"}'
```
Ответ
```bash
curl "http://localhost:8000/reviews?sentiment=negative"
```
