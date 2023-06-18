from ._utils import create_arg
from ._utils import create_config
import smtplib
from env import app_password

class EmailSend:

    config = create_config(
        name="email_send",
        desc="Creates an email and sends it to the recipient",
        required=["to"],
        to=create_arg(
            desc="The recipient/destination. Turn symbols if specified but do not create random symbols. If the email "
                 "is not valid, reprompt the user."
        ),
        subject=create_arg(
            desc="The subject/title of the email. Generate based on body or leave none if specified."
        ),
        body=create_arg(
            desc="The content/body of the email. Generate based on prompts given or leave none if specified."
        )
    )

    @staticmethod
    def run(to, subject=None, body=None):

        if subject is None:
            subject = ""
        if body is None:
            body = ""

        print(f"""to: {to}\nSubject: {subject}\n{body}""")

        EMAIL = "richard.yunqi.zhu@gmail.com"
        PASSWORD = app_password
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=to, 
            msg=f"Subject:{subject}\n\n{body}")
        connection.close()