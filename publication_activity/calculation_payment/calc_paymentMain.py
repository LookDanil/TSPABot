from telebot import types

from comands.start import start
from publication_activity.calculation_payment.monografy import monografy
from user_state import user_state


def typeScienceWork(bot,message):
    user_state['state'] = "typeScienceWork"
    typeScienceWork_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_monografy = types.InlineKeyboardButton("Монография", callback_data='monograph')
    btn_article = types.InlineKeyboardButton("Научная статья", callback_data='article ')

    btn_back = types.KeyboardButton("Назад")
    typeScienceWork_markup.row(btn_monografy, btn_article)
    typeScienceWork_markup.row(btn_back)

    conf_wellcom = ("Укажите тип научной работы для расчёта выплаты: ")

    if message is not None and hasattr(message, 'chat'):
        bot.send_message(message.chat.id, conf_wellcom, reply_markup=typeScienceWork_markup)
    else:
        print(
            "Сообщение не было передано. Пожалуйста, убедитесь, что вы вызываете функцию с правильным объектом сообщения.")
        bot.send_message(message.chat.id, "Произошла ошибка...")
        start()


