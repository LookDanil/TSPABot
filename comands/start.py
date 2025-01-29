from telebot import types
from user_state import user_state
def start(bot, message):
    user_state['state'] = 'start'  # Обновляем состояние
    murkup = types.ReplyKeyboardMarkup(row_width=1)
    btn_konf = types.KeyboardButton("Актуальные конференции")
    murkup.row(btn_konf)
    btn_journal = types.KeyboardButton("Журналы КГЭУ")
    btn_pa = types.KeyboardButton("Публикационная активность")
    murkup.row(btn_pa, btn_journal)

    wellcome = ('Добро пожаловать в чат-бот Центра публикационной активности!\n'
                'В меню вы можете выбрать интересующие вас темы.')


    if message is not None and hasattr(message, 'chat'):
        bot.send_message(message.chat.id, wellcome, reply_markup=murkup)
    else:
        print(
            "Сообщение не было передано. Пожалуйста, убедитесь, что вы вызываете функцию с правильным объектом сообщения.")