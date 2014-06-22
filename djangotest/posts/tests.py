import datetime

from django.utils import timezone
from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from models import Task,Category
from guardian.shortcuts import assign_perm,remove_perm

class TaskTest(TestCase):
    task = None
    def setUp(self):
        testboss = User.objects.create(username='big_boss')
        testuser = User.objects.create(username='joe__test', password='new password')
        category = Category(name="TEST")
        category.save()
        self.task = Task.objects.create(summary='Some job', content='', reported_by=testboss)
        self.task.categories.add(category)

    def test_perms(self):
        user = User.objects.get(username='joe__test')
        boss = User.objects.get(username='big_boss')

        assign_perm('view_task', user, self.task)
        assign_perm('view_task', boss, self.task)
        assign_perm('curate_category', boss, self.task)
        
        self.assertTrue(user.has_perm('view_task', self.task))
        self.assertFalse(user.has_perm('change_task', self.task))

    def tearDown(self):
        user = User.objects.get(username='joe__test')
        boss = User.objects.get(username='big_boss')
        
        remove_perm('view_task', user, self.task)
        remove_perm('view_task', boss, self.task)
        remove_perm('curate_category', boss, self.task)

        self.task.delete()
        user.delete()
        user = User.objects.get(username='big_boss')
        user.delete()
        Category.objects.get(name="TEST").delete()
        
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
        user = User.objects.get(username='john__admin')
        user.delete()
               
