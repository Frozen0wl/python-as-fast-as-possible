import smtplib


def reminder(email):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('pythonmemorize@gmail.com', 'password_2022')

        subject = 'test'
        body = 'this is a test'

        msg = f'Subject: {subject}\n\n{body}'
        
        smtp.sendmail('pythonmemorize@gmail.com', email, msg)
