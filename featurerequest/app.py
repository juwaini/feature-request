from flask import Flask, url_for, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from featurerequest.models import Base, FeatureRequest, Client

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
            {'href': 'feature-request', 'text': 'Feature Request', 'theads': ['date', 'title', 'requester', 'priority']},
            {'href': 'client', 'text': 'Client', 'theads': ['date', 'title', 'requester', 'priority']},
            {'href': 'discussion', 'text': 'Discussion', 'theads': ['date', 'title', 'requester', 'priority', 'status']},
            )

    return render_template('index.html', panels=panels)

@app.route('/login')
def login():
    return 'Please login'

#Route to get whole list

@app.route('/api/feature-requests/', methods=['GET'])
def feature_requests_list():
    """Return JSON list of all feature request."""
    fr = (db.session.query(FeatureRequest).all())
    json_obj = []
    for data in fr:
        json_obj.append({
            'id': data.id,
            'title': data.title,
            'description': data.description
            })
    return jsonify(json_obj)

@app.route('/api/clients/', methods=['GET'])
def clients_list():
    """Return JSON of all clients"""
    clients = (db.session.query(Client).all())
    json_obj = []
    for data in clients:
        json_obj.append({
            'id': data.id,
            'name': data.name
            })
    return jsonify(json_obj)

#Route to get an object based on particular ID
@app.route('/api/feature-request/<int:feature_request_id>', methods=['GET'])
def feature_request_get(feature_request_id):
    """Return JSON of a particular feature request"""
    fr = db.session.query(FeatureRequest).get(feature_request_id)

    if fr:
        json_obj = {'id': fr.id,
                    'title': fr.title,
                    'description': fr.description}
        return jsonify(json_obj)
    else:
        return 'Id %d not exists.' % feature_request_id, 404

@app.route('/api/client/<int:client_id>', methods=['GET'])
def client_get(client_id):
    """Return JSON of a particular client"""
    client = db.session.query(Client).get(client_id)

    if client:
        json_obj = {'id': client.id,
                    'name': client.name,
                    'email': client.email}
        return jsonify(json_obj)
    else:
        return 'Id %d not exists.' % client_id, 404

#Route to create a new object
@app.route('/api/feature-request/create', methods=['POST'])
def feature_request_create():
    """Create a new feature-request"""
    data = request.form
    fr = FeatureRequest(
            title=data['title'], 
            description=data['description'], 
            client=data['client'], 
            client_priority=data['client_priority'],
            #target_date=data['target_date'],
            ticket_url=data['ticket_url'],
            product_area=data['product_area'])
    if fr:
        db.session.add(fr)
        db.session.commit()
        return 'New feature request with id:%d successfully created.' % fr.id
    else:
        return 'Unable to create a new fr.', 404
    return jsonify(data)

@app.route('/api/client/create', methods=['POST'])
def client_create():
    """Create a new client"""
    data = request.form
    client = Client(
            name=data['name'], 
            email=data['email'])
    if client:
        db.session.add(client)
        db.session.commit()
        return 'New client with id:%d successfully created.' % client.id
    else:
        return 'Unable to create a new client.', 404
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
