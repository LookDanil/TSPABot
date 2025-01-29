from user_state import user_state
from telebot import types

def documentation(bot,message):
    user_state['state'] = 'documentations'

    documentation_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_statement = types.KeyboardButton("Заявление на регистрацию")
    btn_monografy = types.KeyboardButton("Соглашение на монографию")
    btn_article = types.KeyboardButton("Соглашение на статью")

    btn_back = types.KeyboardButton("Назад")
    documentation_markup.row(btn_statement, btn_monografy, btn_article)
    documentation_markup.row( btn_back)

    conf_wellcom = ("Тут должен быть текст!")

    if message is not None and hasattr(message, 'chat'):
        bot.send_message(message.chat.id, conf_wellcom, reply_markup=documentation_markup)
    else:
        print(
            "Сообщение не было передано. Пожалуйста, убедитесь, что вы вызываете функцию с правильным объектом сообщения.")