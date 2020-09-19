# pull official base image
FROM python:3.8.5-alpine

# set work directory
WORKDIR /foodgram

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && \
     apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev

# install dependencies
RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/foodgram/entrypoint.sh"]