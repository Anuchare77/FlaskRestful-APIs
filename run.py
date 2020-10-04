from app import app
from db import db

db.init_app(app)

@app.before_first_request   #when used this not necessary to write a codefor create_tables.py
def create_tables():
    db.create_all()