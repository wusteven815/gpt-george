from functions._utils import create_arg
from functions._utils import create_config


class EmailSend:

    config = create_config(
        name="email_send",
        desc="Creates and email and sends it to the recipient",
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
