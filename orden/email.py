from django.core.mail import EmailMessage, get_connection
con = get_connection()

# Отправить сообщения на указанную почту
def send_message(email):
    try:
        con.open()
        em = EmailMessage(subject='Поздравляем', body='Вы назначены на должность руки тьмы', to=[email])
        em.send()
        conn.close()
    except OSError:
        print('Не удалось отправить сообщение')
