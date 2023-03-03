#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py createsuperuser \
--noinput \
--username $DJANGO_SUPERUSER_USERNAME \
--email $DJANGO_SUPERUSER_EMAIL
uvicorn config.asgi:application --host 0.0.0.0 --port 8000

exec "$@"