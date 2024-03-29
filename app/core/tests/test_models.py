from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating new user with an email is successful"""
        email = 'yes@gmail.com'
        password = 'Test12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email given by user is normalized """
        email = 'abs@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """ Test to check email address given by user or not """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating new superuser """
        user = get_user_model().objects.create_superuser(
            'yes@gmail.com',
            'pass@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
