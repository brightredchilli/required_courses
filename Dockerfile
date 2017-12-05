# start from base
# FROM ubuntu:14.04
FROM tiangolo/uwsgi-nginx-flask:python2.7
MAINTAINER Ying Quan Tan <ying.quan.tan@gmail.com>

# The base image, uwsgi-nginx-flask, exposes port 80,
# Installs supervisord, and sets up uwsgi sockets so that all
# that is left to do use a minimal uwsgi.ini

RUN apt-get -yqq update && apt-get install -y \
curl \
vim \
&& rm -rf /var/lib/apt/lists/*

# copy our application code
COPY ./flask-app /app
WORKDIR /app

ENV UWSGI_INI /app/uwsgi.ini

# Copy the entrypoint that will generate Nginx additional configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# fetch app specific deps
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

# start app
CMD ["/usr/bin/supervisord"]
