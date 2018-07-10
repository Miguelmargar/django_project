from django.test import TestCase
from django.urls import reverse
from .views import view_shortlist

# Create your tests here.

class TestAccountsViews(TestCase):
        
    def test_view_shortlist(self):
        response = self.client.get("/shortlist/view")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shortlist/viewshortlist.html")    
        
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/shortlist/view') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('view_shortlist'))
        self.assertEqual(resp.status_code, 200)