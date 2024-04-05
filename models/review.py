#!/usr/bin/python3
"""This script contains review attributes """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey

class Review(BaseModel, Base):
    """ Review class inherits from basemodel and base
    to store review information
    Attributes:
    place_id
    user_id
    text

    """

    __tablename__ = "reviews"
    id = Column(String(60), primary_key=True)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
