#This application requires secure login for accessing the stores dict.
#post(/auth)  generates a JWT(Jason WEb Token) token which can used in GET method

import flask
import flask_jwt
from flask_jwt import JWT,jwt_required
from flask import Flask
import flask_restful
from flask_restful import Api,Resource,reqparse,request
from Flask_app_JWT.security import authentication,identity

app = Flask(__name__)
app.secret_key = 'Anusha'
api = Api(app)
stores = [{'name':'first_store','book':[{'name':'python','cost':99}]}]

jwt = JWT(app,authentication,identity)

class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cost',type=int,required=False,help="This is required field")
    parser.add_argument('name',type=str,required=False)

    @jwt_required()
    def get(self,name):
        for store in stores:
            if store['name'] == name:
                return {'store':store},200
        return {'store not found'},404

    def post(self,name):
        for store in stores:
            if store['name']==name:
                return {"store with the name '{}' exists".format(name)}
            store = {'name':name,'book':[]}
            stores.append(store)
            return store,201

    def delete(self,name):
        global stores
        for store in stores:
            if store['name']!=name:
                stores = dict(store)
        return {'message':'store deleted'}

    def put(self,name):
        data = Store.parser.parse_args()
        for store in stores:
            if store['name']==name:
                store.update(data)
            else:
                store = {'name':name,'book':[]}
                stores.append(store)
        return stores

class StoreList(Resource):
    def get(self):
        return {'stores':stores}

class CreateBookStore(Resource):
    def get(self,name):
        for store in stores:
            if store['name']==name:
                return {'book':store['book']}
        return {'message':'store not found'}

    def post(self,name):
        data = Store.parser.parse_args()
        for store in stores:
            if store['name']==name:
                book = {
                    'name':data['name'],
                    'cost':data['cost']
                }
                store['book'].append(book)
                return (book)
        return {'message':'store not found'}

api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/store')
api.add_resource(CreateBookStore,'/store/<string:name>/book')

#Running the app
app.run(port=5000,debug=True)












