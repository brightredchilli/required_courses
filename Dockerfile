# start from base
# FROM ubuntu:14.04
FROM brightredchilli/uwsgi-nginx-flask:python2.7
MAINTAINER Ying Quan Tan <ying.quan.tan@gmail.com>

# copy our application code
COPY ./flask-app /app
WORKDIR /app

ENV UWSGI_INI /app/uwsgi.ini

# fetch app specific deps
RUN pip install -r requirements.txt && \
python -m textblob.download_corpora
