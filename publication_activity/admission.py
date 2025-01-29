def admission(bot,message):
    with open('Порядок приёма публикаций для формирования приказа на выплату стимулирующей доплаты за публикационную активность.doc', 'rb') as f:
        bot.send_document(message.chat.id, f)