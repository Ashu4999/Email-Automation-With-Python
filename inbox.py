import imaplib
import email
from email.header import decode_header
from datetime import datetime
from datetime import date
from main import *

host = 'imap.gmail.com'
leaveAppArr = []

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

# _, search_data = mail.search(None, 'UNSEEN')

# define since/before dates
date_format = "%d-%b-%Y" # DD-Mon-YYYY e.g., 3-Mar-2014
today = date.today()
datetime_object = datetime.strptime(str(today.month), "%m")
currentMonth = datetime_object.strftime("%b")

since_date = datetime.strptime(f'{today.day}-{currentMonth}-{today.year}', date_format)
before_date = datetime.strptime(f'{today.day+1}-{currentMonth}-{today.year}', date_format)

# get all messages since since_date and before before_date
_, search_data = mail.search(None,'(since "%s" before "%s")' % (since_date.strftime(date_format),before_date.strftime(date_format)))

def getEmails():
    for num in search_data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        senderSubject = decode_header(email_message["Subject"])[0][0]
        if senderSubject == subject:
            senderEmail = decode_header(email_message["From"])[0][0]
            senderEmail = senderEmail.split(" ")[-1].strip("<>")
            leaveAppArr.append(senderEmail)
    return leaveAppArr
