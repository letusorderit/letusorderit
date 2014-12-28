#!/bin/bash
export DJANGO_SETTINGS_MODULE=letusorderit.settings.production
export PYTHONUNBUFFERED=0
mkdir -p /home/uid1000/letusorderit
mkdir -p /home/uid1000/letusorderit/logs
python3 manage.py migrate
python3 manage.py collectstatic --noinput
exec uwsgi --http 0.0.0.0:8000 --wsgi-file /opt/code/letusorderit/letusorderit/wsgi.py --master --processes 4 --threads 2
