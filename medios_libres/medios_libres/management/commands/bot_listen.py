from django.core.management.base import BaseCommand, CommandError
from medios_libres.models import MediosBot

class Command(BaseCommand):
    help = """Listen to Telegram Bot in the background
              (medios_venv)$ python manage.py bot_listen"""

    def handle(self, *args, **options):
        medios = MediosBot()
        medios.bot.polling()
