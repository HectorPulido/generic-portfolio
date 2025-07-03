#!/bin/sh
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py create_default_configs

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi
$@

gunicorn generic_portfolio.wsgi:application --bind 0.0.0.0:8000  --timeout 240 --workers 3 --log-level=debug