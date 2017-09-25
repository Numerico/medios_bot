FROM python:2.7.9

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

WORKDIR /app/medios_libres

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]
