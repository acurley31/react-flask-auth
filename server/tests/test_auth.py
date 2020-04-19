import json
import time
import unittest
import requests

url = 'http://127.0.0.1:5000/api'
url_user_create = url + '/users'
url_login = url + '/login'
url_protected = url + '/protected'

TOKEN_EXPIRATION_SECONDS = 5

class TestUserCRUD(unittest.TestCase):
    
    def setUp(self):
        self.new_user_data = {
            'username': 'firstuser2',
            'first_name': 'Second User',
            'last_name': 'Test',
            'password': 'nksd&asf2',
            'password2': 'nksd&asf2',
        }

    def test_auth_success(self):
        response = requests.post(url_user_create, self.new_user_data)
        data = {
            'username': self.new_user_data['username'],
            'password': self.new_user_data['password'],
        }
        response = requests.post(url_login, data)
        self.assertEqual(response.status_code, 200)
        
        token = response.json().get('token')
        headers = {'Authorization': token}
        response = requests.get(url_protected, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_auth_token_expire(self):
        response = requests.post(url_user_create, self.new_user_data)
        data = {
            'username': self.new_user_data['username'],
            'password': self.new_user_data['password'],
        }
        response = requests.post(url_login, data)
        self.assertEqual(response.status_code, 200)
        
        token = response.json().get('token')
        headers = {'Authorization': token}
        time.sleep(TOKEN_EXPIRATION_SECONDS + 1)
        response = requests.get(url_protected, headers=headers)
        self.assertEqual(response.status_code, 403)

    def test_auth_failure(self):
        response = requests.post(url_user_create, self.new_user_data)
        data = {
            'username': self.new_user_data['username'],
            'password': 'asdfj83rjkjasf',
        }
        response = requests.post(url_login, data)
        self.assertEqual(response.status_code, 401)



if __name__ == '__main__':
    unittest.main()
