import smtplib
from api_keys import app_password

EMAIL = "richard.yunqi.zhu@gmail.com"
PASSWORD = app_password


def sendMail(toAddrs, subject, body):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, 
        to_addrs=toAddrs, 
        msg=f"Subject:{subject}\n\n{body}")
    connection.close()