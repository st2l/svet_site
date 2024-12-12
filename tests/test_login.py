import unittest
from flask import Flask
from flask.testing import FlaskClient
from models import db, User
from routes.login import login
from flask_login import LoginManager


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'bashdbhsbd'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        login_manager = LoginManager()
        login_manager.init_app(self.app)

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        @self.app.route('/login', methods=['GET', 'POST'])
        def login_route():
            return login()

        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_success(self):
        with self.app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('Password1')
            db.session.add(user)
            db.session.commit()

            response = self.client.post('/login', data={
                'email': 'test@example.com',
                'password': 'Password1'
            })
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/')

    def test_login_wrong_password(self):
        with self.app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('Password1')
            db.session.add(user)
            db.session.commit()

            response = self.client.post('/login', data={
                'email': 'test@example.com',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Wrong passwd.', response.data)

    def test_login_nonexistent_user(self):
        response = self.client.post('/login', data={
            'email': 'nonexistent@example.com',
            'password': 'Password1'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'User do not exist.', response.data)
