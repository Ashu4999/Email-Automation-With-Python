from cgitb import html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from operator import truediv
import smtplib

def send_email(email_body='Email Body', from_email='Testing Mail <pmca83440@gmail.com>', subject='Hello World', to_emails=None, html=None, username = None, password = None):
    try:
        if username == None or password == None:
            raise(User_Error("Please Provide Username and Password in send_email() function"))
            return
        assert isinstance(to_emails, list)
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject

        txt_part = MIMEText(email_body, 'plain')
        msg.attach(txt_part)

        if html!=None:
            html_part = MIMEText("<h1>Your Leave Approved</h1>", 'html')
            msg.attach(html_part)

        msg_str = msg.as_string()

        #login to my smtp server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg_str)
        print("Emails sent successfully")
        server.quit()
        # with smtplib.SMTP() as server:
        #     server.login()
        #     pass 
    except User_Error as error:
        print('Error: ', error)


class User_Error(Exception):
   # Constructor method
   def __init__(self, value):
      self.value = value
   # __str__ display function
   def __str__(self):
      return(repr(self.value))