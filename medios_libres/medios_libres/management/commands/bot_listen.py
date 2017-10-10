from django.core.management.base import BaseCommand, CommandError
from medios_libres.models import Texto
import telebot
from telebot import types

# token medios libres
token = "317988596:AAEH2w1RxDYg26hf0aVVFuqtscM7d8dr98Q"

class Command(BaseCommand):
    help = 'Listen to Telegram Bot in the background'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(token)

        mrkp = types.ReplyKeyboardMarkup(row_width=1)
        boton = types.KeyboardButton('Enviar posicion', request_location=True)
        mrkp.add(boton)
 
        @bot.message_handler(commands=['monitor',])
        def query_text(message):
            cid = message.chat.id
            bot.send_message(cid, "Reportar mi ubicacion", reply_markup=mrkp)

        bot.polling()
