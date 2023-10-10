# Выполняем миграции
python manage.py makemigrations
python manage.py migrate

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем Django сервер
gunicorn project.wsgi:application --bind 0:8000