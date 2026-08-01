import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(recipient_email, subject, body):
    """
    Send an email using Gmail SMTP.
    """

    try:
        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email

        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(msg)

        return "Email sent successfully."

    except Exception as e:
        print(e)
        return "Sorry Sagar, I couldn't send the email."