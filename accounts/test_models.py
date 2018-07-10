from django.test import TestCase
from .models import Buyer, Seller
from django.contrib.auth.models import User

# Create your tests here.
class AccountstModelTest(TestCase):
    
    def test_buyer_lable(self):
        user1 = User.objects.create_user(
            username='user1', 
            email='user1@example.com',
            password='password1')
        user = Buyer(user=user1)
        self.assertEqual(str(user), "user1")   
        
    def test_seller_lable(self):
        user1 = User.objects.create_user(
            username='user1', 
            email='user1@example.com',
            password='password1')
        user = Seller(user=user1)
        self.assertEqual(str(user), "user1")    
    
    
        