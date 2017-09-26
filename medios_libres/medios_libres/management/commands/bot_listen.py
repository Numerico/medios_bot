from django.core.management.base import BaseCommand, CommandError
from medios_libres.models import Texto
import telebot

# token medios libres
token = "317988596:AAEH2w1RxDYg26hf0aVVFuqtscM7d8dr98Q"

class Command(BaseCommand):
    help = 'Listen to Telegram Bot in the background'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(token)
        def handle_messages(messages):
            for message in messages:
                Texto.objects.create(texto=message.text)
        bot.set_update_listener(handle_messages)
        bot.polling()

