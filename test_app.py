import unittest
from app import app

class CampusVaultTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"CampusVault", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "healthy")

    def test_add_item(self):
        response = self.client.post(
            "/add",
            data={
                "name": "Lost Keys",
                "category": "Keys",
                "status": "Lost"
            }
        )
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()