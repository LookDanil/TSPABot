from user_state import user_state, state_pay, price_ScienseWork
from telebot import types

def monografy(bot, message):

    state_pay['typeScienceWork'] = 'monografy'
    print(state_pay['typeScienceWork'])

    bot.send_message(message.chat.id, "Введите количество авторов монографии: ")

    def get_authors_count(message):
        try:
            # Пытаемся преобразовать введенное значение в целое число
            authors_count = int(message.text)
            if authors_count > 0:
                # Сохраняем количество авторов в state_pay для текущего пользователя
                state_pay['autors_count'] = authors_count
                bot.send_message(message.chat.id, f"Количество соавторов: {authors_count}")
                bot.send_message(message.chat.id, f"Сумма выплаты за монографию: {price_ScienseWork['monografy']}")
                bot.send_message(message.chat.id, f"Сумма выплаты каждому автору и равном распределении выплаты равно: {price_ScienseWork['monografy'] / authors_count} рублей.")
                # Здесь можно добавить следующий шаг, например, запрос типа статьи
            else:
                bot.send_message(message.chat.id,
                                 "Количество авторов должно быть положительным числом. Попробуйте еще раз.")
                bot.register_next_step_handler(message, get_authors_count)
        except ValueError:
            # Если введенное значение не является числом
            bot.send_message(message.chat.id, "Пожалуйста, введите целое число.")
            bot.register_next_step_handler(message, get_authors_count)

    bot.register_next_step_handler(message, get_authors_count)

    state_pay['type_scienseWork'] = None
    state_pay['autors_count'] = 0
