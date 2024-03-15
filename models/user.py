#!/usr/bin/python3
"""This module defines a class User
    inherits from basemode and
    Base
"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by
    attributes:
    email,
    password,
    first_name and last_name
    """

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
<<<<<<< HEAD
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user")
=======
    first_name = Column(String(128)
    last_name = Column(String(128), nullable)
    places = relationship("Place", cascade='all, delete' backref="user")
    review = relationship("Review", cascade='all, delete' backref="user")
>>>>>>> update place
