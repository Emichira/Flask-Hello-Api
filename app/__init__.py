import os
from flask import Flask, jsonify, request, session, make_response
from flask_restful import reqparse, abort, Resource
from models import User, Book
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity,
    create_access_token, create_refresh_token,
    jwt_refresh_token_required, get_raw_jwt)
from functools import wraps

app =  Flask(__name__)

# Enable blacklisting and specify what kind of tokens to check against the blacklist
app.config['JWT_SECRET_KEY'] = 'hello-api!'  # Change this!
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

user_object = User()
book_object = Book()
blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist
    
@app.errorhandler(400)
def bad_request(error):
    """Custom error handler for bad requests"""
    return jsonify(dict(error = 'Bad request, please add input details')), 400

@app.errorhandler(401)
def unauthorised(error):
    """Custom error handler for bad requests"""
    return jsonify(dict(error = 'Unauthorised, request lacks valid authentication details.')), 401

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for bad requests"""
    return jsonify(dict(error = 'Not Found, resource not found')), 404

@app.errorhandler(500)
def internal_server_error(error):
    """Custom error handler for bad requests"""
    return jsonify(dict(error = 'Internal server error')), 500
    
@app.route('/', methods=['GET'])
def home_route():
    """ HomePage route """
    response = jsonify({'Message': 'Welcome to Hello Library'})
    return response

"""Endpoint for a new user to register."""
@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    if not request.get_json:
        return jsonify({"message": "Please add input details"})
    email = request.json.get('email')
    password = request.json.get('password')
    confirm_password = request.json['confirm_password']
    role = request.json.get('role')

    for user in user_object.user_list:
        if email == user['email'] and password == user['password']:
            response = {"message":"Account already exists"}
            return response

    if email is None:
        return jsonify({'Message': 'Fill in  your email to register'})
    if password is None:
        return jsonify({'Message': 'Fill in  your password to register'})
    if password != confirm_password:
        return jsonify({'message': 'Passwords should match'})
    if (role != 'user') and (role != 'admin'):
        return jsonify({'Message': 'Fill in  your role to register'})
    if len(password) < 8:
        return jsonify({'message': 'password should be more than 8 character'})

    response = jsonify(user_object.register(email, password, confirm_password, role))
    response.status_code = 201
    return response

"""Endpoint for a user to login."""
@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Please add input details"})
    email = request.json.get('email')
    password = request.json.get('password')
    # role = request.json.get('role')
    
    if not email or "":
        return jsonify({'Message': 'Fill in  your email to register'})
    if not password or "":
        return jsonify({'Message': 'Fill in  your password to register'})
        
    for user in user_object.user_list:
        if email == user['email']:
            if password == user['password']:
                token = {
                    'access_token': create_access_token(identity=email)
                }
                return jsonify(token, {"message" : "Login successful"}), 200
            return jsonify({"message":"Password Incorrect"})
        return jsonify({"message":"Email Incorrect"})
    response = jsonify({"message":"User account does not exist, Register account"})
    return response


"""Endpoint for a user reset password."""
@app.route('/api/v1/auth/reset-password', methods=["POST"])
def reset_password():
    email = request.json.get('email')
    new_password = request.json.get('new_password')
    confirm_password = request.json.get('confirm_password')
    
    if request.method == "POST":    
        if email is not None:
            if new_password == confirm_password:
                return jsonify({"message":"Password changed successful"})
        return jsonify({"message": "Password and confirm password should match"})
    return jsonify({"message":"User account does not exist, sign up!"})

"""Endpoint for a user to logout."""
@app.route('/api/v1/auth/logout', methods=["POST"])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200

# Routes for Books
"""Endpoint for adding books and retrieving books."""
@app.route('/api/v1/books', methods=['POST','GET'])
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
        response.status_code = 200
        return response
         
"""Endpoint for finding a book by its ISBN number"""
@app.route('/api/v1/books/ISBN', methods=['GET'])
def get_single_book():

    if session.get('email') is not None:
        if request.method == "GET":
            ISBN = request.json.get('ISBN')
            msg = book_object.get_single_book(ISBN)
            response = jsonify(msg)
            return response
    return jsonify({"message": "Please login"})

"""Endpoint for deleting a book by its ISBN number"""
@app.route('/api/v1/books/ISBN', methods=['DELETE'])
def delete():
    if session.get('title') and session.get('ISBN') is None:
        if request.method == "DELETE":
            title = session["title"]
            ISBN = session['ISBN']
            delete_book = book_object.delete(ISBN, title)
            return jsonify(delete_book)
    return jsonify({"message": "Please login to delete a book"})