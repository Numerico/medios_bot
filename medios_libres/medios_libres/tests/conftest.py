import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medios_libres.settings')

def pytest_configure():
#    settings.DEBUG = False
    settings.IS_TESTING = True
    django.setup()

# FIXTURES
