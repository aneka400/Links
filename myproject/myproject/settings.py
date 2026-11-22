import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасность: читаем из окружения, fallback только для разработки
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-in-production')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') if not DEBUG else ['*']

# Убираем дублирование STATIC_URL
STATIC_URL = 'static/'

# Явно задаём тип первичного ключа — убираем предупреждение Django
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
