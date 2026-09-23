import os
from dotenv import load_dotenv
import smtplib, ssl


load_dotenv()

def send_email(message):
    host ="smtp.gmail.com"
    port = 465

    username = os.getenv('USERNAME')
    password = os.getenv("PASSWORD").strip()

    receiver = os.getenv("RECEIVER")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email('hi')