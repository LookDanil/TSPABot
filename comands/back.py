from journals.journals import journals
from journals.problems_energy.problems import problems
from publication_activity.calculation_payment.calc_paymentMain import typeScienceWork
from publication_activity.public_active import  public_active
from user_state import user_state
from .start import start

def back(bot,message):
    # Словарь для сопоставления состояний и соответствующих функций
    state_functions = {
        'start': start,
        'journals': start,
        'publicActive':start,
        'problems':journals,
        'InfoAurot_problem':problems,
        'journalsList': public_active,
        'documentations':public_active,
        'typeScienceWork':public_active,
        'science_article':typeScienceWork,
        # добавьте другие состояния и функции по мере необходимости
    }
    if user_state['previous_state'] is not None:
        state_functions[user_state['state']](bot, message)
    else:
        bot.send_message(message.chat.id, "Вы находитесь на главном экране, невозможно вернуться назад.")

