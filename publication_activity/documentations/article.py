def article_print(bot,message):
    with open('СОГЛАШЕНИЕ за научную статью.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)