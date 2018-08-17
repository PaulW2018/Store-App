import sqlite3
from db import db


class UserModel(db.Model): # classes now extend db model (inheritance) - these models will be saved and retrieved from a database
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key = True) #id is built in but not a problem in this case. primary_key is auto-incrementing. 
	username = db.Column(db.String(80)) #limit size of string to 80
	password = db.Column(db.String(80))

	
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()


	@classmethod
	def find_by_username(cls,username):
		return cls.query.filter_by(username=username).first() # because there should be only one, so return first.

	@classmethod
	def find_by_id(cls,_id):
		return cls.query.filter_by(id=_id).first()
