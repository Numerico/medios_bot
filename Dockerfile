FROM python:2.7.9

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN chmod u+x medios_libres/entrypoint.sh

RUN pip install -r requirements.txt

WORKDIR /app/medios_libres

EXPOSE 8000

ENTRYPOINT ["/app/medios_libres/entrypoint.sh"]
