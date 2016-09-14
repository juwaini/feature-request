import os
from featurerequest.app import app
import unittest
import tempfile
import requests
import datetime

class FeatureRequestTestCase(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        print(rv)

    def test_create_fr(self):
        form = {'title': 'This is a test title',
                'description': 'A short description for testing.',
                'client': 1,
                'client_priority': 5,
                'target_date': datetime.date.today,
                'ticket_url': 'https://www.google.com',
                'product_area': 'Billings'
                }

        r = requests.post('http://localhost:5000/api/feature-request/create', data=form)
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()
