#!/bin/sh

echo "Waiting for postgres service..."

while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started successfully."

python manage.py run -h 0.0.0.0