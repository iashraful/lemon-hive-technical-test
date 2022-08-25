FROM python:3.9.6-alpine

WORKDIR /api
COPY . /api/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt