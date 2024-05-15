import unittest
from app.api import app

class TestAPI(unittest.TestCase):

    def test_health_check(self):
        tester = app.test_client(self)
        response = tester.get('/api/health', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'status' in response.data)

    def test_slack_endpoint(self):
        tester = app.test_client(self)
        response = tester.post('/api/slack', json={ "message": "Test Message" })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'message' in response.data)

    def test_github_merge_endpoint(self):
        tester = app.test_client(self)
        response = tester.post('/api/github/123', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'message' in response.data)

if __name__ == '__main__':
    unittest.main()

