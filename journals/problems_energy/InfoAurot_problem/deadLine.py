from telebot import types
def deadLine(bot,message):
    with open('Сроки подачи.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
