import telebot
from redoced import redoced
from user_state import user_state

from comands.start import start
from comands.back import back

from publication_activity.journalsList.journalsList import journalsList
from publication_activity.public_active import public_active

from journals.journals import journals
from journals.problems_energy.problems import problems

from conferences.conf import conference
from journals.problems_energy.catigory import catigory_problems
from journals.problems_energy.contacts_problems import contacts_problems
from journals.problems_energy.InfoAurot_problem.InfoAurot_problem import InfoAurot_problem
from journals.problems_energy.InfoAurot_problem.template import template
from journals.problems_energy.InfoAurot_problem.instructions import instructions
from journals.problems_energy.InfoAurot_problem.litra import litra
from journals.problems_energy.InfoAurot_problem.deadLine import deadLine

redoced()
decrypted_token = redoced()
bot = telebot.TeleBot(decrypted_token)

user_state['state'] = 'start'  # Начальное состояние
@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'вернутьсявменю')
@bot.message_handler(commands=['start'])
def handle_start(message):
    start(bot, message)
@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'публикационнаяактивность')
def handle_start(message):
    user_state['state'] = 'publicActive'
    public_active(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'журналыкгэу')
def handle_journals(message):
    journals(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'назад')
def handle_start(message):
    back(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'переченьжурналов')
def handle_journals_list(message):

    journalsList(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'извуз.проблемыэнергетики')
def handle_problems(message):
    problems(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'контакты')
def handle_contacts_problems(message):
    contacts_problems(bot,message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'разделыжурнала')
def handle_catigory_problems(message):
    catigory_problems(bot,message)

@bot.message_handler(func=lambda msg: msg.text == 'Срок подачи')
def handle_deadLine(message):
    deadLine(bot,message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'информациядляавторов')
def handle_InfoAurot_problem(message):
    InfoAurot_problem(bot,message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'инструкциядляотправкистатьи')
def handle_instructions(message):
    instructions(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'оформлениелитературы')
def handle_litra(message):
    litra(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'шаблонстатьи')
def handle_template(message):
    template(bot, message)

@bot.message_handler(func=lambda message: message.text.lower().replace(' ', '') == 'актуальныеконференции')
def handle_conference(message):
    conference(bot, message)

bot.polling(none_stop=True)
