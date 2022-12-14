# syntax=docker/dockerfile:1
FROM ubuntu:focal-20221130
WORKDIR /root
RUN apt-get update && apt-get install -y nginx nano && \
mkdir -p /var/www/html && \
echo "<html><head>Hello World</head><body><h1>Hello World</h1></body></html>" > /var/www/html/index.html

EXPOSE 80 