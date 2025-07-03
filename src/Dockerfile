# pull official base image
FROM python:3.13-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema
RUN apk add --no-cache gcc postgresql-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D myuser
USER myuser