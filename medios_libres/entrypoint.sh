#!/bin/bash

echo "Apply database migrations"
python manage.py migrate

# bot escucha y se despega
python manage.py bot_listen &

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
