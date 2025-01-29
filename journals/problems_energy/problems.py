from telebot import types

from user_state import user_state


def problems(bot,message):
    user_state['state'] = 'problems'
    problem_wellcome = (" Научно-практический рецензируемый журнал "
                        "«Известия высших учебных заведений. ПРОБЛЕМЫ ЭНЕРГЕТИКИ» "
                        "– это рецензируемое научное издание, на страницах которого "
                        "освещаются фундаментальные и прикладные исследования, а также"
                        " дискуссионные вопросы по проблемам энергетики и связанными с"
                        " ней отраслями производства и науки.")

    problem_markup = types.ReplyKeyboardMarkup(row_width=1)

    web_site = types.WebAppInfo('https://www.energyret.ru/jour')
    site = types.KeyboardButton("Ссылка на сайт", web_app=web_site)

    web_last_number = types.WebAppInfo('https://www.energyret.ru/jour/issue/download/69/45')
    last_number = types.KeyboardButton("Последний номер", web_app=web_last_number)

    catigories = types.KeyboardButton("Разделы журнала")

    contacts = types.KeyboardButton("Контакты")

    web_arhive = types.WebAppInfo('https://www.energyret.ru/jour/issue/archive')
    arhive = types.KeyboardButton("Архив", web_app=web_arhive)

    web_news = types.WebAppInfo('https://www.energyret.ru/jour/announcement')
    news = types.KeyboardButton("Новости", web_app=web_news)

    autor_info = types.KeyboardButton("Информация для авторов")

    web_upload_article = types.WebAppInfo('https://www.energyret.ru/jour/author/submit/1')
    insert_article = types.KeyboardButton("Отправить статью", web_app=web_upload_article)

    back_btn = types.KeyboardButton("Назад")

    problem_markup.row(autor_info, catigories, news)
    problem_markup.row(last_number, arhive, contacts)
    problem_markup.row(insert_article, site, back_btn)

    bot.send_message(message.chat.id, problem_wellcome, reply_markup=problem_markup)
