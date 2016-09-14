import os
import unittest
import tempfile
import requests
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from featurerequest.models import Base, FeatureRequest, Client

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Base
db.create_all()
engine = create_engine('sqlite:///testing.db', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class FeatureRequestTestCase(unittest.TestCase):

    url = 'http://localhost:5000'
    database = os.getcwd() + '/testing.db'

    def setUp(self):
        open(self.database, 'a').close()
        #populate_client_database()

    def tearDown(self):
        self.assertEqual('/Users/juwaini/feature-request/testing.db', self.database)
        os.remove(self.database)

    def test_index_page(self):
        r = requests.get(self.url + '/')
        self.assertEqual(r.status_code, 200)

    def test_get_feature_requests(self):
        r = requests.get(self.url + '/api/feature-requests/')
        self.assertEqual(r.status_code, 200)

    def test_get_clients(self):
        r = requests.get(self.url + '/api/clients/')
        self.assertEqual(r.status_code, 200)

    def populate_client_database(self):
        pass

if __name__ == "__main__":
    unittest.main()
