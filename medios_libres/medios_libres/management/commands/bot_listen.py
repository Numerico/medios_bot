from django.core.management.base import BaseCommand, CommandError
from medios_libres.models import Texto, Ubicacion
import telebot
from telebot import types

# token medios libres
token = "317988596:AAEH2w1RxDYg26hf0aVVFuqtscM7d8dr98Q"

class Command(BaseCommand):
    help = 'Listen to Telegram Bot in the background'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(token)

        geo = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        boton = types.KeyboardButton('Enviar posicion', request_location=True)
	geo.add(boton)
 
        @bot.message_handler(commands=['monitor',])
        def mandar_posicion(message):
            """al comando /monitor responde con un teclado con el boton para enviar ubicacion"""
            cid = message.chat.id
            bot.send_message(cid, "Reportar mi ubicacion", reply_markup=geo)

        @bot.message_handler(content_types=['location',])
        def recibir_posicion(message):
            user=message.from_user
            if user.username:
                username = user.username
            elif user.first_name:
                username = user.first_name
            elif user.last_name:
                username = user.last_name
            latitude = message.location.latitude
            longitude = message.location.longitude
            try:
                Ubicacion.objects.create(lat=latitude, longi=longitude, usuario=username)
            except Exception:
                print("falla lat:{}, long:{}, user:{}".format(latitude, longitude, username))
            # TODO FWD

        bot.polling()
