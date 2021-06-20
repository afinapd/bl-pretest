import json
import unittest
import requests


class BasicTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.USERS_URL = 'http://jsonplaceholder.typicode.com/posts'

    def test_get(self):
        self.response_get = requests.get(self.USERS_URL)
        infinite_json = json.loads(self.response_get.text)
        print(type(infinite_json[0]['userId']))
        print(type(infinite_json[0]['id']))
        print(type(infinite_json[0]['title']))
        print(type(infinite_json[0]['body']))
        self.assertEqual(self.response_get.status_code, 200)

    def test_post(self):
        headers = {'Content-Type': 'application/json'}
        payload = {'title': 'test', 'body': 'test', 'userId': 12}
        response_post = requests.post(self.USERS_URL, headers=headers, data=json.dumps(payload, indent=4))
        print(response_post.status_code)
        print(response_post.request)
        print(response_post.text)
        self.assertEqual(response_post.status_code, 201)

if __name__ == "__main__":
    unittest.main()