import pytest
import telebot
from telebot import types
from medios_libres.models import MediosBot, WpPosts, WpUsers
import time

class TestMediosBot:

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.django_use_model(model=[WpPosts, WpUsers])
    def test_receive_text_message(self):
        medios = MediosBot('')
        cmd = self.create_text_message('/publicar algo')
        medios.bot.process_new_messages([cmd])
        time.sleep(0.1) # TODO needs a litte
        assert WpPosts.objects.count() == 1

    # HELPERS

    def create_text_message(self, text):
        params = {'text': text}
        chat = types.User(11, False, 'test')
        #(self, message_id, from_user, date, chat, content_type, options, json_string)
        return types.Message(1, None, None, chat, 'text', params)
