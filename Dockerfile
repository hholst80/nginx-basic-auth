ARG     service=auth-server

FROM    nginx:latest as nginx
COPY    default.conf /etc/nginx/conf.d/
COPY    secret.txt super-secret.txt /etc/nginx/html/

FROM    python:3 as auth-server
RUN     pip install flask
COPY    app.py /app/
WORKDIR /app
CMD     ["flask","run","-h","0.0.0.0"]

FROM    $service
