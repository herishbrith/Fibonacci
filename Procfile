web: python Fibonacci/manage.py collectstatic --noinput; gunicorn Fibonacci.wsgi --log-file --workers=4 --bind=0.0.0.0:8000 Fibonacci/settings.py
