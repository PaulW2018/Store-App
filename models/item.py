
from db import db


class ItemModel(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))
	store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #linking items to stores ForeignKey has id values corresponing to another table - can't delete foreign key items before can delete primary key table. 
	store = db.relationship('StoreModel')	# equivalent to "join" in SQL

	

	def __init__(self, name, price, store_id):
		self.name = name
		self.price = price
		self.store_id = store_id

	def json(self):
		return {'name': self.name, 'price': self.price}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1 - without having to manually do it ourselves!!!

	def save_to_db(self): #useful for both update and insert
		db.session.add(self) # session is a collection of objects to be added to the database
		db.session.commit()


	def delete_from_db(self): # no longer needed
		db.session.delete(self)
		db.session.commit()