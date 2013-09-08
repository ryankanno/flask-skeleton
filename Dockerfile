# 2013-09-08

FROM ubuntu:12.04

MAINTAINER Ryan M. Kanno <ryankanno@localkinegrinds.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install build-essential python python-dev python-pip
RUN mkdir -p /tmp/flask-skeleton
ADD . /tmp/flask-skeleton

RUN pip install -r /tmp/flask-skeleton/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/tmp/flask-skeleton/flask_skeleton/manage.py"]
