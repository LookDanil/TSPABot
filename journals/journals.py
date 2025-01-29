from telebot import types
from user_state import user_state
def journals(bot,message):
    global user_state

    user_state['state'] = 'journals'  # Обновляем глобальное состояние
    print(f'State updated to: {user_state["state"]}')

    journal_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_journal1 = types.KeyboardButton("ИЗВУЗ. ПРОБЛЕМЫ ЭНЕРГЕТИКИ")
    btn_journal2 = types.KeyboardButton("Вестник КГЭУ")
    back = types.KeyboardButton("Назад")
    journal_markup.row(btn_journal1, btn_journal2)
    journal_markup.row(back)

    conf_wellcom = ("Казанский государственный энергетический университет выпускает два научных журнала:"
                    " «ИЗВУЗ. ПРОБЛЕМЫ ЭНЕРГЕТИКИ» и «Вестник КГЭУ».\n "
                    "Данные журналы входят в перечень ВАК по категории К2.")

    bot.send_message(message.chat.id, conf_wellcom, reply_markup=journal_markup)

