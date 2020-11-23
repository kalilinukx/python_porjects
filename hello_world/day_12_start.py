import datetime
import smtplib
from smtplib import SMTPAuthenticationError, SMTPException, SMTP


class MessegeUser():
    user_details = []
    messeges = []
    email_messeges = []
    base_messege = """Hi {name}!
    thanku for the purchase on {date}.
    we hope u are excited about using it.just as a 
    remainder the purchase total was $
    {total}.
    have a great one !
    team flawless
    """

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%0.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail["email"] = email
            self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messeges(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                messege = self.base_messege
                new_msg = messege.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "messege":new_msg
                    }
                    self.email_messeges.append(user_data)
                else:
                    self.email_messeges.append(new_msg)
                self.messeges.append(new_msg)

            return self.messeges
        return []
    def send_email(self):
        self.make_messeges()
        if len(self.email_messeges) > 0:
            for detail in self.email_messeges:
                user_email = detail['email']
                user_messegen = detail['messeges']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    email_conn.sendmail(from_email, to_list, "hello there this is an email messege")
                    email_conn.quit()


obj = MessegeUser()
obj.add_user("justin", 123.92, email="edducationalstyro007@gmail.com")
obj.add_user("jusshgtin", 122.92, email="edducationalstyro007@gmail.com")
obj.add_user("justdgdttin", 125.92, email="edducationalstyro007@gmail.com")
obj.add_user("justgfdin", 173.92, email="edducationalstyro007@gmail.com")
obj.add_user("justorin", 133.92, email="edducationalstyro007@gmail.com")
obj.get_details()

obj.make_messeges()
