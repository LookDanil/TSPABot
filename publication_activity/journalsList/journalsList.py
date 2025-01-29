from telebot import types
from user_state import user_state

def journalsList(bot,message):
    user_state['state'] = 'journalsList'
    journalsList_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_whiteList = types.KeyboardButton("Белый список")
    btn_RINCList = types.KeyboardButton("Список ядра РИНЦ")
    btn_VAKList = types.KeyboardButton("Перечень ВАК")
    btn_journalCatigory = types.KeyboardButton("Журналы по категориям")
    btn_back = types.KeyboardButton("Назад")

    # Исправлено: убрали journalsList_markup
    journalsList_markup.row(btn_whiteList, btn_RINCList)
    journalsList_markup.row(btn_VAKList, btn_journalCatigory, btn_back)

    conf_wellcom = ("Тут должен быть текст!")

    bot.send_message(message.chat.id, conf_wellcom, reply_markup=journalsList_markup)
