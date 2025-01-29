def contacts_problems(bot,message):
    post_contacts = ("Редакция журнала «Известия высших учебных заведений. ПРОБЛЕМЫ ЭНЕРГЕТИКИ»\n"
                     "Казанский государственный энергетический университет\n"
                     "г. Казань, ул. Красносельская, 51\n"
                     "Телефон: +7(843) 527-92-76\n"
                     "E-mail: problems_ener@mail.ru")
    bot.send_message(message.chat.id, post_contacts)
