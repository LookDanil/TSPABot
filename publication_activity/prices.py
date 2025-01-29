def prices(bot,message):
    with open('Расчет выплат.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)