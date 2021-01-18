FROM python:3.8-slim

RUN apt-get update && apt-get -y install \
    default-libmysqlclient-dev \
    gcc

RUN pip install --upgrade pip

RUN pip install Django==3.1.3
RUN pip install djangorestframework==3.12.2
RUN pip install django-cors-headers==3.5.0
RUN pip install mysqlclient

WORKDIR /django

CMD ["python"]
