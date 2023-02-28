# zmekhyxmmpuztzrp
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Shahrooz Aghili'
email['to'] = 'shahrooz33ce@gmail.com'
email['subject'] = 'Welcome to America!'

email.set_content(html.substitute({'name': 'Roosie'}), 'html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    email_address = 'shahrooz33ce@gmail.com'
    email_password = ''
    connection.login(email_address, email_password)
    connection.send_message(email)
