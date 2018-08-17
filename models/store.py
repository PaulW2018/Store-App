from db import db


class StoreModel(db.Model):
	__tablename__ = 'stores'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel', lazy='dynamic') #back reference - list of item models
	

	def __init__(self, name):
		self.name = name
		
	def json(self):
		return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1 - without having to manually do it ourselves!!!

	def save_to_db(self): #useful for both update and insert
		db.session.add(self) # session is a collection of objects to be added to the database
		db.session.commit()


	def delete_from_db(self): # no longer needed
		db.session.delete(self)
		db.session.commit()