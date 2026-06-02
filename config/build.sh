#!/usr/bin/env bash
# exit on error
set -o errexit

cd .. # 👈 أضف هذا السطر هنا للعودة إلى المجلد الرئيسي حيث يوجد requirements.txt

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
