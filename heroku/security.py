#contains important functions it has in memory table for user
from heroku_flask.models.user import UserModel

#Authenticate user funnctin
def aunthentication(username,password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)