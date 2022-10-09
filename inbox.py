import imaplib
import email
from email.header import decode_header
from datetime import datetime

host = 'imap.gmail.com'
username =  'pmca83440@gmail.com'
password = 'oiilyvynmcblmtap'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

# _, search_data = mail.search(None, 'UNSEEN')

# define since/before dates
date_format = "%d-%b-%Y" # DD-Mon-YYYY e.g., 3-Mar-2014
since_date = datetime.strptime('9-Oct-2022', date_format)
before_date = datetime.strptime('10-Oct-2022', date_format)

# get all messages since since_date and before before_date
_, search_data = mail.search(None,'(since "%s" before "%s")' % (since_date.strftime(date_format),before_date.strftime(date_format)))
_, search_data = mail.search(None, before_date.strftime(date_format))

print(search_data)

for num in search_data[0].split():
    _, data = mail.fetch(num, '(RFC822)')
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    date = decode_header(email_message["Subject"])[0][0]
    print(date)
