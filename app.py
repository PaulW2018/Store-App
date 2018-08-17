
from flask_jwt import JWT
from flask import Flask
from flask_restful import Api 

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turn of Flask modification tracker. 
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWT(app, authenticate, identity) # /auth - sends a username and password


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': # only file that we run is __main__
	from db import db  # to avoid circular imports
	db.init_app(app)
	app.run(port=5000, debug=True)









