FROM python

WORKDIR /app
COPY . .

RUN pip install django gunicorn

RUN ln -sf /app/bash-4.3 /bin/sh
EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "django_shellshock.wsgi:application"]
