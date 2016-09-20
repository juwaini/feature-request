import os
import unittest
import tempfile
import requests
from datetime import date

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from featurerequest.models import Base, FeatureRequest, Client

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db'


class FeatureRequestTestCase(unittest.TestCase):

    url = 'http://localhost:5000'
    database = os.getcwd() + '/testing.db'

    def setUp(self):
        # Use Flask-SQLAlchemy for its engine and session
        # configuration. Load the extension, giving it the app object,
        # and override its default Model class with the pure
        # SQLAlchemy declarative Base class.
        self.db = SQLAlchemy(app)
        self.db.Model = Base
        self.db.create_all()
        engine = create_engine('sqlite:///testing.db', echo=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
       
        #open(self.database, 'a').close()
        self.db.create_all()
        #self.populate_client_database()

    def tearDown(self):
        self.db.drop_all()
        #self.assertEqual('/Users/juwaini/feature-request/testing.db', self.database)
        #os.remove(self.database)

    def test_index_page(self):
        r = requests.get(self.url + '/')
        self.assertEqual(r.status_code, 200)

    def test_get_feature_requests(self):
        r = requests.get(self.url + '/api/feature-request/')
        self.assertEqual(r.status_code, 200)

    def test_get_clients(self):
        r = requests.get(self.url + '/api/client/')
        print(r.json())
        self.assertEqual(r.status_code, 200)

    def test_get_one_client(self):
        r = requests.get(self.url + '/api/client/1')
        #print(r.json())
        self.assertEqual(r.status_code, 404)

    def populate_client_database(self):
        self.db.session.add(Client(name='Microsoft', email='test@microsoft.com'))
        self.db.session.commit()
        self.db.session.add(Client(name='Google', email='test@google.com'))
        self.db.session.commit()
        self.db.session.add(Client(name='Yahoo', email='test@yahoo.com'))
        self.db.session.commit()

if __name__ == "__main__":
    unittest.main()
