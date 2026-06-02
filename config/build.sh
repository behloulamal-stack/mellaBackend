#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput  #t3 css
python manage.py migrate
