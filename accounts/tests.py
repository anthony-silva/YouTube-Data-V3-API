from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.conf import settings

User = get_user_model()

# Create your tests here. 
class UserTestCase(TestCase):

    def setUp(self): # Python's builtin unittest 
        user_a = User(username='cfe', email='cfe@invalid.com')
        user_a_pwd = 'some_123_password'
        self.user_a_pwd = user_a_pwd
        user_a.is_staff = True 
        user_a.is_superuser = True 
        user_a.set_password(user_a_pwd)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self): # function name must begin with test_
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        user_a = User.objects.get(username="cfe")
        self.assertTrue(user_a.check_password(self.user_a_pwd))

