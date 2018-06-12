import telebot
from medios_libres.models import WpPosts, WpUsers
from datetime import datetime

# TODO ENV KEY
medios_bot = telebot.TeleBot('')

def fetch_message_author(message):
# TODO user matching WP/Telegram
# bot_user = self.bot.get_me()
# for now we use a bot user in wp
    wp_post_author, created = WpUsers.objects.get_or_create(
        user_login = "mediosbot",
        user_pass = "sanJuanGariguna",
        user_nicename = "medios_bot",
        user_email = "bot@numerica.cl",
        user_url = "",
        user_registered = datetime.now(),
        user_activation_key = "",
        user_status = 1,
        display_name = "MediosBot",
    )
    return wp_post_author

@medios_bot.message_handler(commands=['publicar',])
def listen_publicar(message):
    hoy=datetime.now()
    post_author = fetch_message_author(message)
    wp_post = WpPosts.objects.create(
        post_content=message.text,
        #defaults
        post_author=post_author.id,
        post_date=hoy,
        post_date_gmt=hoy,
        post_modified=hoy,
        post_modified_gmt=hoy,
        post_parent=0,
        menu_order=0,
        comment_count=0,
    )
