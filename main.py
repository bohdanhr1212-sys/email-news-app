import os
from dotenv import load_dotenv
import smtplib, ssl
import requests

load_dotenv()

letter = {"title": [], "text":" ", "link":" ", "letter_theme": " ","sort":" "}

api = os.getenv('API')
url = os.getenv('URL')

requests = requests.get(url)
content = requests.json()

#print(content['articles'])

for article in content['articles']:
    letter['title'].append(article['title'])

def send_email(message):
    host ="smtp.gmail.com"
    port = 465

    username = os.getenv('EUSERNAME')
    password = os.getenv("PASSWORD")

    receiver = os.getenv("RECEIVER")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

send_email(letter['title'])