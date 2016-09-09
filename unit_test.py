import os
from index import app
import unittest
import tempfile

class FeatureRequestUnitTest(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, index.app.config['DATABASE'] = tempfile.mkstemp()
        index.app.config['TESTING'] = True
        self.app = index.app.test_client()
        with index.app.app_context():
            index.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(index.app.config['DATABASE'])

if __name__ == "__main__":
    unittest.main()
