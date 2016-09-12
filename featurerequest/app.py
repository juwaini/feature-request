from flask import Flask, url_for, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from featurerequest.models import Base, FeatureRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Base

@app.route('/')
def index():
    panels = (
            {'href': 'feature-request', 'text': 'Feature Request', 'theads': ['date', 'title', 'requester', 'priority']},
            {'href': 'discussions', 'text': 'Discussions', 'theads': ['date', 'title', 'requester', 'priority', 'status']},
            )

    return render_template('index.html', panels=panels)

@app.route('/login')
def login():
    return 'Please login'

@app.route('/api/feature-requests/', methods=['GET'])
def feature_requests_list():
    """Return JSON list of all feature request."""
    fr = (db.session.query(FeatureRequest).all())
    return jsonify(fr)

@app.route('/api/feature-request/<int:feature_request_id>', methods=['GET'])
def feature_request_get(feature_request_id):
    """Return JSON of a particular feature request"""
    fr = db.session.query(FeatureRequest).get(feature_request_id)
    return jsonify(fs)

@app.route('/api/feature-request/create', methods=['POST'])
def feature_request_create():
    """Create a new feature-request"""
    data = request.form
    fr = FeatureRequest(data['field'], data['description'])
    db.session.add(fr)
    db.session.commit()
    return jsonify(request.form)

if __name__ == '__main__':
    app.run(debug=True)
