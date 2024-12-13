import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from conf import Config
from loguru import logger


def send_email(to_address, subject, message):
    """
    Sends an email using the specified parameters.
    
    :param to_address: The recipient's email address.
    :type to_address: str
    :param subject: The subject of the email.
    :type subject: str
    :param message: The body of the email.
    :type message: str
    :raises Exception: If there is an error sending the email.
    :return: None
    """
    

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
        
        logger.info("Email sent successfully")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")
