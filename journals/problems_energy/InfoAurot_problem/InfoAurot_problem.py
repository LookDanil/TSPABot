from telebot import types

from user_state import user_state


def InfoAurot_problem(bot,message):
    user_state['state'] = 'InfoAurot_problem'
    markdown = """
                *bold text*
                _italic text_
                [text](URL)
                """
    marcup = types.ReplyKeyboardMarkup(row_width=1)

    web_rules = types.WebAppInfo('https://www.energyret.ru/jour/about/submissions#authorGuidelines')
    rules_btn = types.KeyboardButton("Правила", web_app=web_rules)

    template_btn = types.KeyboardButton("Шаблон статьи")
    instructions_btn = types.KeyboardButton("Инструкция для отправки статьи")
    litra_btn = types.KeyboardButton("Оформление литературы")
    deadLine_btn = types.KeyboardButton("Срок подачи")
    web_upload_btn = types.WebAppInfo('https://www.energyret.ru/jour/author/submit/1')
    uploadArticle_btn = types.KeyboardButton("Отправить статью", web_app=web_upload_btn)

    back = types.KeyboardButton("Назад")
    mainMenu_btn = types.KeyboardButton("Вернуться в меню")
    marcup.row(rules_btn, template_btn, instructions_btn)
    marcup.row(litra_btn, deadLine_btn, uploadArticle_btn)
    marcup.row(back, mainMenu_btn)

    text_message = ("Полный текст статьи приводится на русском или английском языке. "
                    "В статье должны быть четко обозначены актуальность, научная значимость, методология,"
                    " цель исследования, результаты и выводы,"
                    " а также исчерпывающий анализ современной литературы. "
                    "\n\n"
                    "Статья должна быть структурирована по международной системе IMRAD и включать в себя: "
                    "Введение (Introduction), Литературный обзор (Literature Review), Материалы и методы"
                    " (Materials and methods), Результаты (Results), Обсуждение (Discussions), "
                    "Заключение или Выводы (Conclusions)."
                    "\n\n"
                    "*Объем статьи должен быть не менее 12 страниц, включая аннотацию и библиографический список.*"
                    "\n\n"
                    "*Для прохождения входного контроля программой Антиплагиат, показатель оригинальности должен составлять 80-85%.*"
                    "\n\n"
                    "К рукописи статьи прилагаются:\n "
                    "– сопроводительное письмо от организации, в которой выполнена работа;\n "
                    "– экспертное заключение о возможности опубликования статьи в открытой печати;\n "
                    " – для сотрудников КГЭУ выписка из протокола заседания кафедры.\n"
                    "\n\n"
                    "Электронный вариант рукописи статьи с полным комплектом документов загружаются в редакцию через https://www.energyret.ru")
    bot.send_message(message.chat.id, text_message, parse_mode="markdown", reply_markup=marcup)



