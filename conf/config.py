import os
from dotenv import load_dotenv

# load the local env variables
load_dotenv()


class Config:

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
