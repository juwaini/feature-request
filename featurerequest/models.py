from flask import Flask

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///sqlite3.db', echo=True)

class FeatureRequest(Base):
    __tablename__ = 'feature_requests'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True)
    description = Column(String(2000))
    client = Column(Integer)
    client_priority = Column(Integer)
    target_date = Column(DateTime)
    ticket_url = Column(String(80))
    product_area = Column(String(10))

    def __repr__(self):
        return '<Feature Request: %r>' % self.title

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

