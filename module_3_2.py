def send_email(message, recipient, sender='university.help@gmail.com'):

    ''' подфункция для проверки правильности адреса '''
    def is_valid_email(email):
        if '@' in email and email.endswith('.com') or email.endswith('.ru') or email.endswith('.net'):
            return True
        return False

    # print(is_valid_email(recipient))

    # проверка адресов (использую втроенную функцию)
    if not is_valid_email(recipient) and is_valid_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    # проверка на отправку самому себе (использую втроенную функцию)
    if recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
        return

    # проверка отправителя по умолчанию (использую втроенную функцию)
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return


send_email('Это сообщение для проверки связи', 'ikl1337@gmail.com')
send_email('Это сообщение для проверки связи', 'ikl1337@gmail.com', sender='urban.info@gmail.com')
send_email('Это сообщение для проверки связи', 'urban.student@mail.uk', sender='university.help@gmail.com')
send_email('Это сообщение для проверки связи', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')