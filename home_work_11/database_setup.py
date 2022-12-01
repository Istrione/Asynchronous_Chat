import sys
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

engine = create_engine('sqlite:///storage.db')

class Client(Base):
    __tablename__='clients'

    id=Column(Integer, primary_key=True)
    login=Column(String)
    info=Column(String)
    contacts=relationship('Contact_List')

    def __repr__(self):
        return "<Client(login='%s', info='%s', contacts='%s')>" % (
            self.login,
            self.info,
            self.contacts,
        )

class Owner(Base):
    __tablename__='owner'

    id=Column(Integer, primary_key=True)
    contacts=relationship('Contact_List', backref='owner', uselist=False)

    def __repr__(self):
        return "<Owner(contacts='%s')>" % (
            self.contacts,
        )

class Client_Story(Base):
    __tablename__='client_story'

    id=Column(Integer, primary_key=True)
    login=Column(DateTime, default=datetime.now)
    ip_adress=Column(String)

    def __repr__(self):
        return "<Client_Story(login='%s', ip_adress='%s')>" % (
            self.login,
            self.ip_adress,
        )

class Contact_List(Base):
    __tablename__='contact_list'

    id=Column(Integer, primary_key=True)
    owner_id=relationship('Owner')
    client_id=Column(Integer, ForeignKey('clients.id'))

    def __repr__(self):
        return "<Contact_List(owner_id='%s', client_id='%s')>" % (
            self.owner_id,
            self.client_id,
        )

Base.metadata.create_all(engine)