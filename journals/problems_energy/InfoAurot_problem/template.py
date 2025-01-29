def template(bot,message):
    with open('Шаблон статьи.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)


