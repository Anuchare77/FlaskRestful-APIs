#Always run create_tables.py file before running app_ex.py file then data.db is created. Initially there will be no data.db file

from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from Dynamic_db_for_users.security import aunthentication,identity
from Dynamic_db_for_users.user import UserRegister

app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

jwt = JWT(app,aunthentication,identity)   #in memory database

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this field cannot br blank")

    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x:x['name']==name,items),None)
        return {'item':item},200 if item else 404

    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None):
            return {'meassage':"An item with the name '{}' already exists".format(name)},400 #400 is bad request this is clients problem that he requested for the item that already exists

        request_data = Item.parser.parse_args()
        item = {'name':name,'price':request_data['price']}
        items.append(item)
        return item,201

    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name']!=name,items))
        return {'message':'Item deleted'}

    def put(self,name):
        request_data = Item.parser.parse_args()
        # item = next(filter(lambda x:x['name']==name,items),None)
        # print(item)
        for item in items:
            if item['name']==name:
                item.update(request_data)
            else:
                item = {'name': name, 'price': request_data['price']}
                items.append(item)
        return items

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000,debug=True)


#In postman first use post('/item/auth') this end point is created by jwt extension,give username and password same as in in memory database. This generates a token.copy paste that
#secondly use post('/item/piano') to create a new item in list
#Thirdly use get('/item/piano') this asks for authentication, now in the header use Key as Authentication and value as JWT copy paste token above here



