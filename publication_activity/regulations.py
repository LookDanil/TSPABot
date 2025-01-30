def regulation(bot,message):
    with open(
            'Регламент.docx',
            'rb') as f:
        bot.send_document(message.chat.id, f)
