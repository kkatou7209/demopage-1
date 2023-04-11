FROM python:3.12.0a7-alpine3.17

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt

RUN apk add --no-cache uwsgi uwsgi-python3
RUN pip install -r requirements.txt

CMD ["uwsgi", "wsgi.ini"]