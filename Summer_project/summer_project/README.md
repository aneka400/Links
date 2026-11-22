# MyProject

Django-проект с формой приветствия.

## Быстрый старт

```bash
# 1. Установить зависимости
pip install -r requirements.txt

# 2. Настроить переменные окружения
cp .env.example .env
# Отредактировать .env — сменить SECRET_KEY

# 3. Применить миграции
python manage.py migrate

# 4. Создать суперпользователя (для /admin)
python manage.py createsuperuser

# 5. Запустить сервер
python manage.py runserver
```

Откройте http://127.0.0.1:8000/
