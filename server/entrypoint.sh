#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do 
       sleep 0.1
    done

   echo "PostgreSQL started"
fi

./manage.py flush --no-input
./manage.py migrate
./manage.py runserver 0.0.0.0:8000

exec "$@"
