# Hello Docker

Простое Flask-приложение, упакованное в Docker.

## Сборка
docker build -t hello-docker .

## Запуск
docker run -d --name hello-docker -p 5000:5000 hello-docker

## Открыть в браузере
http://localhost:5000
