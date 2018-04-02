import os
from flask import Flask, jsonify, request, session, abort, make_response, render_template
from flask_restful import reqparse, abort, Resource
from models import User, Book
from run import create_app

user = [
        {
            'email': 'abc@abc.com',
            'password': '12345678',
            'role': 'user'
        },
        {
            'email': 'emmanuel@abc.com',
            'password': '87654321',
            'role': 'admin'
        }
        ]

book = [
        {
            'ISBN': 00001,
            'title': 'MacBeth',
            'author': 'William Shakespear',
            'date_published': '02/02/2018',
            'category': 'History'
        },
        {
            'ISBN': 00002,
            'title': 'Long Walk To Freedom',
            'author': 'Nelson Mandela',
            'date_published': '02/02/2018',
            'category': 'Biography'
        }
    ]

user_list = []
new_user={}
books_list=[]
user_dict = {}

user_object = User()
book_object = Book()

@create_app.route('/')
def home_route():
    """ HomePage route """
    response = jsonify({'Message': 'Welcome to Hello Library'})
    return response

"""Endpoint for a new user to register."""
@create_app.route('/api/v1/auth/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    confirm_password = request.json['confirm_password']
    role = request.json.get('role')

    if email is None:
        return jsonify({'Message': 'Fill in  your email to register'})
    elif password is None:
        return jsonify({'Message': 'Fill in  your password to register'})
    elif (role != 'user') and (role != 'admin'):
        return jsonify({'Message': 'Fill in  your name to register'})
    if len(password) < 8:
        return jsonify({'message': 'password should be more than 8 character'})

    msg = user_object.register(email, password, confirm_password, role)
    response = jsonify(msg)
    response.status_code = 200
    return response

"""Endpoint for a user to login."""
@create_app.route('/api/v1/auth/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    session['email'] = email and session['password'] == password
    msg = user_object.login(email, password)
    response = jsonify(msg)
    response.status_code = 200
    return response

"""Endpoint for a user reset password."""
@create_app.route('/api/v1/auth/reset-password', methods=["POST"])
def reset_password(email,password,confirm_password):
    if session.get('email') is not None:
        if request.method == "POST":
            new_password = request.json['new_password']
            confirm_password = request.json['confirm_password']
            msg = user_object.reset_password(new_password, confirm_password)
            return msg
    return jsonify({"message": "User account does not exist, sign up"})

"""Endpoint for a user to logout."""
@create_app.route('/api/v1/auth/logout', methods=["POST"])
def logout():
    if session.get("email") is not None:
        session.pop("email", None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"}) 

# Routes for Books
"""Endpoint for adding books and retrieving books."""
@create_app.route('/api/v1/books', methods=['POST','GET'])
def add_book():
    if request.method == "POST":
        ISBN = request.json.get('ISBN')
        title = request.json.get('title')
        author = request.json.get('author')
        date_published = request.json.get('date_published')
        category = request.json.get('category')

        msg = book_object.add_book(ISBN, title, author, date_published, category)
        response = jsonify(msg)
        response.status_code = 201
        return response
    elif request.method == "GET":
        msg = book_object.get_all()
        response = jsonify(msg)
        return response
         
"""Endpoint for finding a book by its ISBN number"""
@create_app.route('/api/v1/business/ISBN', methods=['GET'])
def get_single_book(ISBN):

    if session.get('email') is not None:
        if request.method == "GET":
            msg = book_object.get_single_book(ISBN)
            response = jsonify(msg)
            return response
    return jsonify({"message": "Please login to get business"})

"""Endpoint for deleting business by its ISBN number"""
@create_app.route('/api/v1/business/ISBN', methods=['DELETE'])
def delete(ISBN):
    if session.get('title') is not None:
        if request.method == "DELETE":
            title = session["title"]
            delete_book = book_object.delete(ISBN, title)
            return jsonify(delete_book)
    return jsonify({"message": "Please login to delete a book"})

if __name__ == '__main__':
    create_app.run(debug=True)

    


