# Pull base image
FROM python:3.9.6-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# install psycopg2 dependencies
RUN pip install --upgrade pip
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

# Install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --no-cache --virtual .build-deps build-base linux-headers
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . /app