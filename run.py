# from app import User, Book
# from app import reset_password, login, register, logout, add_book
from flask import Flask
from flask_restful import Resource, Api

create_app = Flask(__name__)

if __name__ == '__main__':
    
    create_app.run(debug=True)

