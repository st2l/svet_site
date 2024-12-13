
## Svet-site

Site for internet-shop for street lights.

It is on github ***ONLY for educational purposes***!!!
It can't be used by anyone without [author](https://github.com/st2l) permission

## Deploy

1) Creation of the configuration file

Create `.env` file that contains:

```

DATABASE_URL="sqlite:///database.db"
SECRET_KEY="123456"  # for local deploy
ADMIN_NAME="admin"
ADMIN_EMAIL="aaa@gmail.com"
ADMIN_PASSWD="123456"

# for system email
MAIL_SERVER="smtp.gmail.com"
MAIL_PORT=587
SYSTEM_EMAIL="example@gmail.com"
SYSTEM_EMAIL_PASSWD="123465"

# for manager email
MANAGER_EMAIL="manager@gmail.com"

```

> If you are deploying your site on a remote hosting -> change this things to actual ones.

2) Installing requirements.txt

```

pip install -r requirements.txt

```

3) Running the application

```python

python ./app.py

```
