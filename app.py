from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
# we tell where the database is located (at the root)
# it doesn't have to be sqlite, it could be mysql, ...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# this only change the behavior of the extensions
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'enric'
api = Api(app)

@app.before_first_request
def create_table():
  db.create_all()

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/chair
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items') # http://127.0.0.1:5000/items
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# python names the file run as __main__
# for example, if we run >python app.py -> app (this file) would be main
# however, if we access this file from another file by importing it, this piece of code will not be run

if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(port=5000, debug=True)