import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()




class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(Integer, nullable=False)
    birth_date = Column(Integer,unique=True, nullable=False)
    email = Column(String(30),unique=True, nullable=False)
    password = Column(String(30))
    id_adress = Column(String(100), unique = False, nullable = False)
    phone = Column(Integer,unique=True, nullable=False)
    user_rol = Column(Integer, unique = False, nullable = False)
    is_active = Column(Boolean(), unique=False, nullable=False)



class Owner(Base):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer)

class Buddy(Base):
    __tablename__ = 'buddy'
    id = Column(Integer, primary_key=True)
    service = Column(String(30))
   
    
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    id_comment = Column(String(200))
    

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_body= Column(String(200))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')