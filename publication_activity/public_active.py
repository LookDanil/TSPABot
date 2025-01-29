from user_state import user_state
from telebot import types
def public_active(bot,message):
    user_state['state'] = 'publicActive'

    publicActive_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_regulations = types.KeyboardButton("Регламент")
    btn_reception = types.KeyboardButton("Порядок приема")
    btn_documentation = types.KeyboardButton("Документация")
    btn_pay = types.KeyboardButton("Расчёт выплаты")
    btn_journalsList = types.KeyboardButton("Перечень журналов")
    btn_back = types.KeyboardButton("Назад")
    publicActive_markup.row(btn_reception, btn_documentation, btn_pay)
    publicActive_markup.row(btn_regulations, btn_journalsList, btn_back)

    conf_wellcom = ("Тут должен быть текст!")

    if message is not None and hasattr(message, 'chat'):
        bot.send_message(message.chat.id, conf_wellcom, reply_markup=publicActive_markup)
    else:
        print(
            "Сообщение не было передано. Пожалуйста, убедитесь, что вы вызываете функцию с правильным объектом сообщения.")
