def litra(bot,message):
    with open('Правила оформления литературы.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)
