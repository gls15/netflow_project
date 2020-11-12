# Source: https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development

import smtplib, ssl

def notify(recipient, body):
    port = 465

    # SMTP server (here, it is GMail)
    smtp_server = "smtp.gmail.com"

    # Sender email address (must match SMTP server)
#    sender = <sender_gmail_address>
    sender = input("Enter sender GMail address: ")

    # Password for sender email account
#    password = <sender_gmail_password>
    password = input("Enter password: ")

    # Email content
    subject = "NVCAT: Summary Report"
    message = "Subject: "+subject+"\r\n"+body

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, message)

