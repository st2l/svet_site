import os
from dotenv import load_dotenv

# load the local env variables
load_dotenv()


class Config:
    """
    Класс Config содержит конфигурационные параметры для приложения.
    Атрибуты:
        SQLALCHEMY_DATABASE_URI (str): URI базы данных, полученный из переменной окружения 'DATABASE_URL'.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Флаг для отслеживания изменений в SQLAlchemy, по умолчанию False.
        SECRET_KEY (str): Секретный ключ для CSRF и шифрования данных, полученный из переменной окружения 'SECRET_KEY'.
        ADMIN_NAME (str): Имя администратора, полученное из переменной окружения 'ADMIN_NAME'.
        ADMIN_EMAIL (str): Email администратора, полученный из переменной окружения 'ADMIN_EMAIL'.
        ADMIN_PASSWD (str): Пароль администратора, полученный из переменной окружения 'ADMIN_PASSWD'.
        UPLOAD_FOLDER (str): Путь к папке для загрузки файлов, по умолчанию './static/img'.
        MAIL_SERVER (str): Сервер для отправки почты, полученный из переменной окружения 'MAIL_SERVER'.
        MAIL_PORT (str): Порт для отправки почты, полученный из переменной окружения 'MAIL_PORT'.
        SYSTEM_EMAIL (str): Системный email для отправки почты, полученный из переменной окружения 'SYSTEM_EMAIL'.
        SYSTEM_EMAIL_PASSWD (str): Пароль для системного email, полученный из переменной окружения 'SYSTEM_EMAIL_PASSWD'.
        MANAGER_EMAIL (str): Email менеджера, полученный из переменной окружения 'MANAGER_EMAIL'.
    """


    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # Поддержка удаленной БД
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Для CSRF и шифрования данных
    SECRET_KEY = os.environ.get('SECRET_KEY')

    ADMIN_NAME = os.environ.get('ADMIN_NAME')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
    ADMIN_PASSWD = os.environ.get('ADMIN_PASSWD')
    UPLOAD_FOLDER = './static/img'

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    SYSTEM_EMAIL = os.environ.get('SYSTEM_EMAIL')
    SYSTEM_EMAIL_PASSWD = os.environ.get('SYSTEM_EMAIL_PASSWD')
    
    MANAGER_EMAIL = os.environ.get('MANAGER_EMAIL')
