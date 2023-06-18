import smtplib

EMAIL = "richard.yunqi.zhu@gmail.com"
PASSWORD = "borugldqumzdtrdh"


def sendMail(toAddrs, subject, body):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, 
        to_addrs=toAddrs, 
        msg=f"Subject:{subject}\n\n{body}")
    connection.close()