#Always run create_tables.py file before running app_ex.py file then data.db is created. Initially there will be no data.db file
#In this case we are retreiving contents of item from database
from flask import Flask,request
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import aunthentication,identity
from resources.user import UserRegister
from resources.items import Item,ItemList
from resources.store import StoreList,Store
from models.store import StoreModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = 'Anusha'
api = Api(app)

@app.before_first_request   #when used this not necessary to write a codefor create_tables.py
def create_tables():
    db.create_all()

jwt = JWT(app,aunthentication,identity)   #in memory database

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':

    db.init_app(app)
    app.run(port=5000,debug=True)




