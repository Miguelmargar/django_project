from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductModelTest(TestCase):
    
    def test_name_lable(self):
        product = Product(name="Moonphase")
        self.assertEqual(str(product), "Moonphase")   
        
    
        