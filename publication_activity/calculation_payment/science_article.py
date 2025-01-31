from comands.start import start
from user_state import state_pay, user_state
from telebot import types

def science_article(bot, message):
    user_state['state'] = "science_article"
    state_pay['typeScienceWork'] = 'science_article'
    print(state_pay['typeScienceWork'])

    typeArticle_markup = types.ReplyKeyboardMarkup(row_width=1)

    btn_RINC = types.InlineKeyboardButton("РИНЦ", callback_data='RINC')
    btn_VAK = types.InlineKeyboardButton("ВАК", callback_data='VAK ')
    btn_Scopus = types.InlineKeyboardButton("Scopus", callback_data='Scopus ')
    btn_back = types.KeyboardButton("Назад")

    typeArticle_markup.row(btn_RINC, btn_VAK,btn_Scopus)
    typeArticle_markup.row(btn_back)

    conf_wellcom = ("Укажите тип научной статьи: ")

    def get_type_article(message):
        
        return message.text

    if message is not None and hasattr(message, 'chat'):
        bot.send_message(message.chat.id, conf_wellcom, reply_markup=typeArticle_markup)
    else:
        print(
            "Сообщение не было передано. Пожалуйста, убедитесь, что вы вызываете функцию с правильным объектом сообщения.")
        bot.send_message(message.chat.id, "Произошла ошибка...")
        start()

    type_article = bot.register_next_step_handler(message, get_type_article)