from app import User, Book
# from app import reset_password, login, register, logout, add_book
from flask import Flask, request
from flask_restful import Resource, Api

create_app = Flask(__name__)
api = Api(create_app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    
    create_app.run(debug=True)

