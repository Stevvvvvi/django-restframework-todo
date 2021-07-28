from django.test import TestCase
from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
    def test_test(self):
        self.assertEqual(1,1-0)
    
    def test_creates_user(self):
        user=User.objects.create_user('hi','hi@gmail.com', 'test123')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email, 'hi@gmail.com')
        self.assertFalse(user.is_staff)
    
    def test_creates_superuser(self):
        user=User.objects.create_superuser('hi','hi@gmail.com', 'test123')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email, 'hi@gmail.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
    def test_raise_error_no_username(self):
        with self.assertRaisesMessage(ValueError, 'The given password must be set'): 
            User.objects.create_user('hi','hi@gmail.com','')
        
        # self.assertIsInstance(user,User)
        # self.assertEqual(user.email, 'hi@gmail.com')
        # self.assertTrue(user.is_staff)
        # self.assertTrue(user.is_superuser)