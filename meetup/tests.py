from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.


class LoginTest(TestCase):
    pass
    # def setUp(self):
    #     self.credentials = {
    #         'username': 'joey',
    #         'password': 'Joey@123!'}
    #     User.objects.create_user(**self.credentials)
    # def test_login(self):
    #     # send login data
    #     response = self.client.post('/login/', self.credentials, follow=True)
    #     # should be logged in now
    #     self.assertTrue(response.context['user'].is_active)

