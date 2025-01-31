def monografy_doc(bot,message):
    with open('СОГЛАШЕНИЕ монография.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)