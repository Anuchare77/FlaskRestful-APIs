#Always run create_tables.py file before running app_ex.py file then data.db is created. Initially there will be no data.db file
#In this case we are retreiving contents of item from database
from flask import Flask,request
from flask_restful import Api
from flask_jwt import JWT
from Create_itemresrc_indb.security import aunthentication,identity
from Create_itemresrc_indb.user import UserRegister
from Create_itemresrc_indb.item import Item,ItemList

app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

jwt = JWT(app,aunthentication,identity)   #in memory database

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000,debug=True)


