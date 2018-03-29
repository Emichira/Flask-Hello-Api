import os
from flask import Flask, jsonify, abort, make_response, request, render_template, session
from flask_restful import reqparse, abort, Resource
from models import User, Book
from run import create_app

user = []
user_list = []
new_user={}
books_list=[]

@create_app.route('/api/v1/auth/login', methods=['POST'])
def login(email,password):
    for user in user_list:
        if user["email"]==email and user["password"]==password:
            return jsonify({'message': "you have successfully logged in"})
            
        else:
            return jsonify({'error': "Invalid email or password"})

@create_app.route('/api/v1/auth/reset-password', methods=["POST"])
def reset_password(email,password,confirm_password):
    for user in User.user_list:
        if user["email"] == email:
            if password == confirm_password:
                user["password"]=password
                user["confirm_password"]=confirm_password            
                return jsonify({'message': "Password reset was successful"})

            else:
                
                return jsonify({'message': "Password and confirm password must be the same"})
        else:
            
            return jsonify({'message': "Account does not exist"})

@create_app.route('/api/v1/auth//register', methods = ['GET' , 'POST'])
def register(email, password):
    if request.method == 'POST':
        if new_user["password"] == new_user["password"]:
            return jsonify({'message': "successfully registered user"})
    else:
        return jsonify({'message': "Invalid password, sign upto create an account"})

@create_app.route('/api/v1/auth/logout', methods=["POST"])
def logout():
    """this endpoint will logout the user"""

    if session.get("email") is not None:
        session.pop("email", None)
        return jsonify({"message": "Logout successful"})
    return jsonify({"message": "You are not logged in"}) 

@create_app.route('/api/v1/books', methods=['POST','GET'])
def add_book():
        if request.method == 'POST':
            ISBN = request.json.get('ISBN')
            title = request.json.get('title')
            author = request.json.get('author')
            date_published = request.json.get('date_published')
            category = request.json.get('category')

            if ISBN and title and author and date_published and category:
                response=jsonify(books_list.append(ISBN, title, author, date_published, category))
                response.status_code=201
                return response

            else:
                response=jsonify({"message":"enter all details","status_code":400})
                response.status_code=200
                return response            
        
if __name__ == '__main__':
    create_app.run(debug=True)

    


