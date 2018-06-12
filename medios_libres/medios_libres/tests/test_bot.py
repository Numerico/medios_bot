import pytest
from telebot import types
from medios_libres.models import WpPosts, WpUsers
import time # TODO needs a litte
from medios_libres.bot import medios_bot

class TestMediosBot:

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.django_use_model(model=[WpPosts, WpUsers])
    def test_no_receive_text(self):
        cmd = self.create_text_message('solo algo')
        medios_bot.process_new_messages([cmd])
        time.sleep(0.1)
        assert WpPosts.objects.count() == 0

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.django_use_model(model=[WpPosts, WpUsers])
    def test_receive_command(self):
        cmd = self.create_text_message('/publicar algo')
        medios_bot.process_new_messages([cmd])
        time.sleep(0.1)
        assert WpPosts.objects.count() == 1

    # HELPERS

    def create_text_message(self, text):
        params = {'text': text}
        chat = types.User(11, False, 'test')
        #(self, message_id, from_user, date, chat, content_type, options, json_string)
        return types.Message(1, None, None, chat, 'text', params)
