def statement(bot,message):
    with open('Заявление.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)