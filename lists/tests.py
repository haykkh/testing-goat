from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
