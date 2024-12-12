import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from conf import Config


def send_email(to_address, subject, message):
    from_address = Config.SYSTEM_EMAIL
    password = Config.SYSTEM_EMAIL_PASSWD

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        server.starttls()
        server.login(from_address, password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
