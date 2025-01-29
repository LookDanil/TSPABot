def instructions(bot,message):
    with open('Инструкция для отправки статьи.pdf', 'rb') as f:
        bot.send_document(message.chat.id, f)


