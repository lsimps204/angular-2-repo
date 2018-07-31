FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /code/requirements.txt

COPY . /code/

RUN pip install -r /code/requirements.txt

WORKDIR /code/

EXPOSE 8000