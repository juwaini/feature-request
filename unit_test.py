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
        db.create_all()
        self.populate_client_database()

    def tearDown(self):
        db.drop_all()
        self.assertEqual('/Users/juwaini/feature-request/testing.db', self.database)
        os.remove(self.database)

    def test_index_page(self):
        r = requests.get(self.url + '/')
        self.assertEqual(r.status_code, 200)

    def test_get_feature_requests(self):
        r = requests.get(self.url + '/api/feature-request/')
        self.assertEqual(r.status_code, 200)

    def test_get_clients(self):
        r = requests.get(self.url + '/api/client/')
        self.assertEqual(r.status_code, 200)

    def test_get_one_client(self):
        r = requests.get(self.url + '/api/client/1')
        self.assertEqual(r.status_code, 404)

    def populate_client_database(self):
        db.session.add(Client(name='Microsoft', email='test@microsoft.com'))
        db.session.commit()
        db.session.add(Client(name='Google', email='test@google.com'))
        db.session.commit()
        db.session.add(Client(name='Yahoo', email='test@yahoo.com'))
        db.session.commit()

if __name__ == "__main__":
    unittest.main()
