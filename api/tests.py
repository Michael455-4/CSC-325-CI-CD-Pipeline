from django.test import TestCase
from django.urls import reverse


class ApiTests(TestCase):
    def test_health_endpoint(self):
        response = self.client.get(reverse('health'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})

    def test_echo_endpoint(self):
        response = self.client.get(reverse('echo'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Hello from CSC 325!')
        self.assertEqual(response.json()['version'], '2.0')
        self.assertEqual(response.json()['course'], 'CSC 325')
        self.assertEqual(response.json()['status'], 'active')
        self.assertEqual(response.json()['pipeline'], 'CI/CD')
        
        
        
        

       

       






