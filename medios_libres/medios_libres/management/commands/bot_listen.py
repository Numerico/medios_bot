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
        boton = types.KeyboardButton('Enviar posicion')#, request_location=True) TODO cell
	geo.add(boton)
 
        @bot.message_handler(commands=['monitor',])
        def mandar_posicion(message):
            """al comando /monitor responde con un teclado con el boton para enviar ubicacion"""
            cid = message.chat.id
            bot.send_message(cid, "Reportar mi ubicacion", reply_markup=geo)
            # FIXME x testing
            bot.send_location(cid, 14.232, -90.282)

        @bot.message_handler(content_types=['location',])
        def recibir_posicion(message):
            username = message.from_user.username
            latitude = message.location.latitude
            longitude = message.location.longitude
            Ubicacion.objects.create(lat=latitude, longi=longitude, usuario=username)
            # TODO FWD

        bot.polling()
