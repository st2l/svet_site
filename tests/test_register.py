import unittest
from flask import Flask
from flask.testing import FlaskClient
from models import db, User
from routes.register import register, validate_email, validate_password


class RegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        @self.app.route('/register', methods=['GET', 'POST'])
        def register_route():
            return register()

        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_validate_email(self):
        self.assertTrue(validate_email('test@example.com'))
        self.assertFalse(validate_email('invalid-email'))

    def test_validate_password(self):
        self.assertTrue(validate_password('Password1'))
        self.assertFalse(validate_password('password'))
        self.assertFalse(validate_password('Password'))
        self.assertFalse(validate_password('password1'))

    def test_register_success(self):
        with self.app.app_context():
            response = self.client.post('/register', data={
                'username': 'testuser',
                'email': 'test@example.com',
                'password': 'Password1'
            })
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, '/login')
            self.assertIsNotNone(User.query.filter_by(
                username='testuser').first())

    def test_register_empty_username(self):
        response = self.client.post('/register', data={
            'username': '',
            'email': 'test@example.com',
            'password': 'Password1'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Username cannot be empty.', response.data)

    def test_register_invalid_email(self):
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'invalid-email',
            'password': 'Password1'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid email.', response.data)

    def test_register_invalid_password(self):
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            b'Password must be at least 8 characters long, contain at least one digit, and at least one uppercase letter.', response.data)

    def test_register_existing_username(self):
        with self.app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('Password1')
            db.session.add(user)
            db.session.commit()

            response = self.client.post('/register', data={
                'username': 'testuser',
                'email': 'new@example.com',
                'password': 'Password1'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn(
                b'A user with this username already exists.', response.data)
