from inbox import *
from send_email import *

username =  'ashuepic99@gmail.com'
password = 'uokweivrbjhmewgw'
subject = 'Leave Application'
email_subject = 'Leave Applicatio Response'
email_from = 'helixstackHr@gmail.com'
email_body = 'Your Leave Approved\nPlease commit you changes before leaving from office'
# html="<h1>This is testing for html</h1>" //send this as parameter in html default parameter for html

if __name__ == "__main__":
    leaveAppArr = []
    leaveAppArr = getEmails()
    send_email(to_emails=leaveAppArr, subject=email_subject, from_email=email_from, email_body=email_body, username=username, password=password)