import json
import unittest
import requests

url = 'http://127.0.0.1:5000/api'
url_list_create = url + '/users'
url_detail = url + '/users/{}'


class TestUserCRUD(unittest.TestCase):
    
    def setUp(self):
        self.new_user_data = {
            'username': 'firstuser2',
            'first_name': 'Second User',
            'last_name': 'Test',
            'password': 'nksd&asf2',
            'password2': 'nksd&asf2',
        }

    def test_a_user_create(self):
        response = requests.post(url_list_create, self.new_user_data)
        self.assertEqual(response.status_code, 201)

    def test_b_user_get(self):
        user_id = '1'
        url = url_detail.format(user_id)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get('username'), 
            self.new_user_data.get('username'))

    def test_c_user_update(self):
        user_id = '1'
        url = url_detail.format(user_id)
        data = {'username': 'mynewusername', 'first_name': 'Michael'}
        response = requests.patch(url, data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get('first_name'), 'Michael')

    def test_d_user_delete(self):
        user_id = '1'
        url = url_detail.format(user_id)
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data, {'id': user_id})


if __name__ == '__main__':
    unittest.main()
