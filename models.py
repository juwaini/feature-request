from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from index import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db.sqlite3'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

app = Flask(__name__)
db = SQLAlchemy(app)

class FeatureRequest(db.Model):
    __tablename__ = 'feature-requests'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(2000))
    #client = db.Column(db.Integer, db.ForeignKey('users.id'))
    client_priority = db.Column(db.Integer)
    target_date = db.Column()
    ticket_url = db.Column(db.String(80))

    def __repr__(self):
        return '<Feature Request: %r>' % self.title
    
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<Client: %r>' % self.name

