#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
import models


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            
            if 'updated_at' not in kwargs:
                self.created_at = datetime.now()
            else:
                kwargs['updated_at'] = datetime.fromisoformat(kwargs
                                                              ['updated_at'])
            if 'created_at' not in kwargs:
                self.updated_at = datetime.now()
            else:
                kwargs['created_at'] = datetime.fromisoformat(kwargs
                                                              ['created_at'])

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "__class__" in self.__dict__:
                del self.__dict__["__class__"]
        models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if dictionary['_sa_instance_state']:
                del dictionary['_sa_instance_state']

        return dictionary
    
    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
        models.storage.save()