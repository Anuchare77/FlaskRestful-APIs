#this app has a test.py file which creates username and pw in data.db file
import flask
from flask import Flask
import flask_jwt
from flask_jwt import JWT,jwt_required
import flask_restful
from flask_restful import Resource,Api,reqparse
from Static_user_db.security import authentication,identity

app = Flask(__name__)
app.secret_key = 'Anusha'
api = Api(app)

jwt = JWT(app,authentication,identity)
items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type = float,required = True,help = "This field cannot be blank")

    @jwt_required()
    def get(self,name):
        for item in items:
            if item['name']==name:
                return {'item':item},200
        return {'message':'item not found'},404

    def post(self,name):
        for item in items:
            if item['name']==name:
                return {'message':"An item with name '{}' already exists".format(name)}
        data = Item.parser.parse_args()
        new_item = {'name':name,'price':data['price']}
        items.append(new_item)
        return new_item,201

    #delete not working
    def delete(self,name):
        global items
        for item in items:
            if item['name']!=name:
                items = list(item)
            return {'message':'Item deleted'}
        return {'message':'Item not found'}

    def put(self,name):
        data = Item.parser.parse_args()
        for item in items:
            if item['name']==name:
                item.update(data)
            else:
                new_item ={'name':name,'price':data['price']}
                items.append(new_item)
        return items

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000,debug=True)
