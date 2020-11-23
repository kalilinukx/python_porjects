import smtplib
from smtplib import SMTPAuthenticationError, SMTPException, SMTP
host = "smtp.gmail.com"
port = 587
password = ""
username = "educationalstyro007@gmail.com"
from_email = username
to_list=["educationalstyro007@gmail.com"]
email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "hello there this is an email messege")
email_conn.quit()

from smtplib import SMTP

ABC = smtplib.SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "hello this an email messege")
ABC.quit()
pass_wrong=SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrong password")
    pass_wrong.sendmail(from_email, to_list, "hi")
except SMTPAuthenticationError:
    print("an error occured")
except:
    print("could not login")


pass_wrong.quit()
# it is mendatory for users to switch on the less security on email service
