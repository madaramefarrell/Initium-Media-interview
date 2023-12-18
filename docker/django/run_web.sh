#!/bin/sh

./wait-for-it.sh pg:5432 -t 2
cd /code/ && python manage.py migrate
cd /code/ && python manage.py runserver 0.0.0.0:8000
