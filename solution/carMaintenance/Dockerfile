FROM python:3.9-bullseye

#Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y --no-install-recommends \
unixodbc-dev \
unixodbc \
libpq-dev 

COPY /requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /djangoBackend

COPY ./djangoBackend /djangoBackend
WORKDIR /djangoBackend

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
RUN chmod 777 -R /djangoBackend

USER user

CMD python manage.py makemigrations && \
python manage.py collectstatic --no-input && \
python manage.py migrate && \
gunicorn djangoBackend.wsgi:application --bind 0.0.0.0:8000
