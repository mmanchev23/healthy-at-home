FROM python:3.12-slim

WORKDIR /server

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN --mount=type=secret,id=_env,dst=/etc/secrets/.env cp /etc/secrets/.env /server/.env

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

RUN python manage.py createsuperuser --noinput || true

EXPOSE 80

CMD [ "gunicorn", "api.wsgi:application", "-b", "0.0.0.0:80", "-w", "8" ]
