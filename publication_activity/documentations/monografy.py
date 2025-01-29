def monografy(bot,message):
    with open('СОГЛАШЕНИЕ монография.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)