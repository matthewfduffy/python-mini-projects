"""
    Function to send emails.
    Do not use this to send client emails.
    Sender must always be yourself or a shared mailbox you own.
    Email is a string or a list of recipients

    Required Packages:
    # import smtplib, pandas, email.message, email, utils
"""
import smtplib
import pandas as pd
from email.message import EmailMessage
from email.utils import make_msgid


def send_html_email(sender, reciever, subject, body, cc, attachment=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever
        # for multiple users, create a list
    msg['Cc'] = cc

    image_cid = make_msgid()
    msg.set_content('')
    msg.add_alternative(f"""\
    <html>
        <head></head>
        <body>
            <p>{body}</p>
        </body>
    </html>    
        """, subtype='html')

    if not attachment == None:
        with open(attachment, 'rb') as fp:
            attach_data = fp.read()
            ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            filename=attachment.split('/')[-1].split('\\')[-1]
            msg.add_attachment(attach_data, maintype=maintype, subtype=subtype, filename=filename)

    with smtplib.SMTP('mailhost.company.net:25') as s:
        s.send_message(msg)