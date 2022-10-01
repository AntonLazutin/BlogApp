FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

EXPOSE 8001

RUN pip install -r requirements.txt

CMD python manage.py runserver localhost:8000