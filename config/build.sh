#!/usr/bin/env bash
cd config
pip install -r requirements.txt
python manage.py collectstatic --noinput  #t3 css
python manage.py migrate
# إنشاء حساب مسؤول تلقائياً إذا لم يكن موجوداً من قبل
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'AmelSecurePass2026')"
