FROM python:3.8-alpine


ENV PYTHONUNBUFFERED 1

RUN mkdir /DOCKERAPP
WORKDIR /DOCKERAPP
COPY ./APP /DOCKERAPP


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN adduser -D nirajkhatiwada
USER nirajkhatiwada