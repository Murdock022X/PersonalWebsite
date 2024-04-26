FROM python:slim-buster

WORKDIR /var

RUN mkdir app

WORKDIR /var/app

COPY website website
COPY app.py app.py
COPY gunicorn_config.py gunicorn_config.py
COPY requirements.txt requirements.txt

RUN mkdir /var/log/gunicorn
RUN touch /var/log/gunicorn/gunicorn.access.log
RUN touch /var/log/gunicorn/gunicorn.error.log

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "app:app", "-c", "gunicorn_config.py"]
