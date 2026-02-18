import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_python():
    sender = os.environ.get('EMAIL_SENDER')
    receiver = os.environ.get('EMAIL_RECEIVER')
    subject = "One course opened"
    message = "one course is opened"

    password="EMAIL_APP_PASSWORD" # Not email password it is email app password
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, msg.as_string())
        print("Successfully sent email")
        smtpObj.quit()
    except Exception as e:
        print(e)

send_email_python()