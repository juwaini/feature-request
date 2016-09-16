from flask import Flask, url_for, render_template, request, jsonify
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from featurerequest.schema import FeatureRequestSchema, ClientSchema

from featurerequest.models import Base, FeatureRequest, Client

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Base
db.create_all()
engine = create_engine('sqlite:///sqlite3.db', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    panels = (
            {'href': 'feature-request', 'text': 'Feature Request', 'theads': ['ID', 'Title', 'Client', 'Priority']},
            {'href': 'client', 'text': 'Client', 'theads': ['ID', 'Name', 'Email']},
            {'href': 'discussion', 'text': 'Discussion', 'theads': ['date', 'title', 'requester', 'priority', 'status']},
            )

    return render_template('index.html', panels=panels)

@app.route('/login')
def login():
    return 'Please login'

#API to generate client dropdown
@app.route('/api/dropdown/<string:table>/', methods=['GET'])
def generate_client_dropdown(table):
    if table == 'client':
        clients = db.session.query(Client).all()

    result = []

    for client in clients:
        data = dict(id=client.id, name=client.name)
        result.append(data)
        
    return jsonify(result)

#API to generate datatables
@app.route('/api/datatables/<string:table>/', methods=['GET'])
def generate_client_table(table):
    if table == 'client':
        rows = (db.session.query(Client).all())
    elif table == 'feature-request':
        rows = (db.session.query(FeatureRequest).all())

    result = []
    for row in rows:
        if table == 'client':
            data = row.id, row.name, row.email
        elif table == 'feature-request':
            data = row.id, row.title, row.description, row.client
        result.append(data)
    return jsonify({'data': result})

#Route to get whole list or a particular feature-request
@app.route('/api/feature-request/<int:feature_request_id>', methods=['GET'])
@app.route('/api/feature-request/', methods=['GET'])
def get_feature_requests(feature_request_id=None):
    """Return JSON list of all/particular feature request."""
    if feature_request_id:
        fr = db.session.query(FeatureRequest).get(feature_request_id)
        if not fr:
            return "Resource not found.", status.HTTP_404_NOT_FOUND
        return jsonify({'feature-request': fr})
    fr = (db.session.query(FeatureRequest).all())
    return jsonify({'feature-request': fr})

@app.route('/api/client/<int:client_id>', methods=['GET'])
@app.route('/api/client/', methods=['GET'])
def get_clients(client_id=None):
    """Return JSON of all/particular clients"""
    if client_id:
        client = db.session.query(Client).get(client_id)
        if not client:
            return "Resource not found.", status.HTTP_404_NOT_FOUND
        data = dict(id=client.id, name=client.name, email=client.email)
        schema = ClientSchema()
        result = schema.dump(data)
        return jsonify(result.data)
    clients = (db.session.query(Client).all())
    result = []
    for client in clients:
        data = dict(id=client.id, name=client.name, email=client.email)
        schema = ClientSchema()
        result.append(schema.dump(data).data)
    return jsonify(result)

#Route to create a new object
@app.route('/api/feature-request/create', methods=['POST'])
def feature_request_create():
    """Create a new feature-request"""
    data = request.get_json(force=True)
    fr = FeatureRequest()
    fr.title = data['title']
    fr.description = data['description']
    fr.client = data['client']
    db.session.add(fr)
    db.session.commit()
        
    return 'New feature request with id:%d successfully created.' % (fr.id), status.HTTP_200_OK

@app.route('/api/client/create', methods=['POST'])
def client_create():
    """Create a new client"""
    data = request.get_json(force=True)
    client = Client()
    client.name = data['name']
    client.email = data['email']
    db.session.add(client)
    db.session.commit()

    return 'New client with id:%d successfully created.' % (client.id), status.HTTP_200_OK

if __name__ == '__main__':
    app.run(debug=True)
