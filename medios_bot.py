import telebot
# token medios libres
token = "317988596:AAEH2w1RxDYg26hf0aVVFuqtscM7d8dr98Q"
bot = telebot.TeleBot(token)

def handle_messages(messages):
    for message in messages:
        print(message.text)

bot.set_update_listener(handle_messages)
bot.polling()
