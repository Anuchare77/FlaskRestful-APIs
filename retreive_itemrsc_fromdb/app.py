#Always run create_tables.py file before running app_ex.py file then data.db is created. Initially there will be no data.db file
#In this case we are retreiving contents of item from database
from flask import Flask,request
from flask_restful import Api
from flask_jwt import JWT
from retreive_itemrsc_fromdb.security import aunthentication,identity
from retreive_itemrsc_fromdb.user import UserRegister
from retreive_itemrsc_fromdb.item import Item,ItemList

app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

jwt = JWT(app,aunthentication,identity)   #in memory database

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000,debug=True)


#In postman first use post('/item/auth') this end point is created by jwt extension,give username and password same as in in memory database. This generates a token.copy paste that
#secondly use post('/item/piano') to create a new item in list
#Thirdly use get('/item/piano') this asks for authentication, now in the header use Key as Authentication and value as JWT copy paste token above here



