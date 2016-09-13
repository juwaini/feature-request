from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, Date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///sqlite3.db', echo=True)
app = Flask(__name__)

class FeatureRequest(Base):
    __tablename__ = 'feature_requests'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True)
    description = Column(String(2000))
    client = Column(Integer)
    client_priority = Column(Integer)
    #target_date = Column(Date)
    ticket_url = Column(String(80))
    product_area = Column(String(10))

    def __repr__(self):
        return '<Feature Request:(title=%s, description=%s, client=[KIV])>' % (
                self.title, self.description)

if __name__ == "__main__":
    import sqlalchemy
    print('sqlalchemy version:' + sqlalchemy.__version__)

    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///sqlite3.db', echo=True)
