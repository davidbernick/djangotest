import datetime

from django.utils import timezone
from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class UserMethodTests(TestCase):
    
    def setUp(self):
        user = User.objects.create_user('john__admin', 'lennon@thebeatles.com', 'johnpassword')
        user.set_password('new password')
        user.save()

    def test_login_user(self):
        user = authenticate(username='john__admin', password='new password')
        self.assertTrue(user)

    def test_login_bad_user(self):
        user = authenticate(username='john__admin', password='bad password')
        self.assertFalse(user)
        
    def tearDown(self):
        user = authenticate(username='john__admin', password='new password')
        user.delete()
               
