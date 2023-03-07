#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate --noinput
uvicorn config.asgi:application --host 0.0.0.0 --port 8000

exec "$@"