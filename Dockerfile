FROM python:3.8

MAINTAINER Aqueduct <hello@aqueducthq.com> version: 0.0.1

RUN pip install requests

ENV PYTHONUNBUFFERED 1

COPY install_aqueduct.py /install_aqueduct.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]