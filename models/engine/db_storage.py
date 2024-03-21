#!/usr/bin/python3

""" DBStorage module for the HBNB project 
    This module defines a class DBStorage
    that inherits from BaseStorage
    
    example:
    storage = DBStorage()
    storage.reload()
	storage.all()
	storage.new(obj)
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage():
	"""This class defines a DBStorage class
	that inherits from BaseStorage

	Attributes:
		__engine: None
		__session: None

	Methods:
		__init__(self): constructor
		all(self, cls=None): returns a dictionary
		new(self, obj): adds a new object to the session
		save(self): commits all changes of the current session
		delete(self, obj=None): deletes an object from the current session
		reload(self): creates all tables in the database

	Returns:
		None
	"""
	
	__engine = None
	__session = None

	def __init__(self):
		"""Constructor for DBStorage class
		creates the engine and session
		"""

		user = os.getenv('HBNB_MYSQL_USER')
		pwd = os.getenv('HBNB_MYSQL_PWD')
		host = os.getenv('HBNB_MYSQL_HOST')
		db = os.getenv('HBNB_MYSQL_DB')

		self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
									  .format(user, pwd, host, db),
									  pool_pre_ping=True)
		if os.getenv('HBNB_ENV') == "test":
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""Returns a dictionary of models currently in storage
		 
		Args:
			cls: class name

		Returns:
			dictionary of models currently in storage
		   """
		classes = [State, City, User, Place, Amenity, Review]
		storage_dict = {}
		if cls:
			if cls in classes:
				objects = self.__session.query(cls).all()
				for obj in objects:
					key = "{}.{}".format(obj.__class__.__name__, obj.id)
					storage_dict[key] = obj
			return storage_dict
		else:
			for cls in classes:
				objects = self.__session.query(cls).all()
				for obj in objects:
					key = "{}.{}".format(obj.__class__.__name__, obj.id)
					storage_dict[key] = obj
			return storage_dict
		
	def new(self, obj):
		"""Adds new object to storage dictionary
		
		Args:
			obj: object to be added to storage dictionary
		
		Returns:
			None
		"""
		self.__session.add(obj)

	def save(self):
		"""Saves storage dictionary to file
		
		Returns:
			None
		"""
		self.__session.commit()
	
	def delete(self, obj=None):
		"""Delete obj from __objects if it’s inside
		
		Args:
			obj: object to be deleted
		
		Returns:
			None
		"""
		if obj:
			self.__session.delete(obj)

	def reload(self):
		"""Loads storage dictionary from file
		
		Returns:
			None
		"""
		Base.metadata.create_all(self.__engine)
		Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
		self.__session = scoped_session(Session)