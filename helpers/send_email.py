import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from conf import Config
from loguru import logger


def send_email(to_address, subject, message):
    """
    Отправляет электронное письмо на указанный адрес.
    Параметры:
        to_address (str): Адрес электронной почты получателя.
        subject (str): Тема письма.
        message (str): Текст сообщения.
    Исключения:
        Exception: Если отправка письма не удалась, выбрасывается исключение с описанием ошибки.
    Возвращает:
        None
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
