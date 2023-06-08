FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /app

COPY ./app /app

CMD [ "python", "./main.py" ]