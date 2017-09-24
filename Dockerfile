FROM python:2.7.9

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

CMD ["python", "medios_bot.py"]
