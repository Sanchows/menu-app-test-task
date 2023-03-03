FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/project .
RUN python manage.py collectstatic

COPY ./entrypoint-web.sh .

RUN chmod +x entrypoint-web.sh

ENTRYPOINT ["./entrypoint-web.sh"]