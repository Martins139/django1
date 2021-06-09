from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class homepageTest(TestCase):
    def get_status_code(self):
        response=self.client.get.reverse("home")
        self.assertEqual(response.status_code, 200)
        self.asertTemplateUsed(response,'home.html')
