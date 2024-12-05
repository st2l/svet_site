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
