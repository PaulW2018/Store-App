
import os #access to OS environmeent variables

from flask_jwt import JWT
from flask import Flask
from flask_restful import Api 

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')  #use sqlite if locally running on a machine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turn of Flask modification tracker. 
app.secret_key = 'jose'
api = Api(app)



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










