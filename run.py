from app import reset_password, login, register, logout, add_book, delete, get_single_book
from flask import Flask, jsonify, request, session, abort, make_response, render_template
from flask_restful import Resource, Api
from flask_restful import reqparse, abort, Resource
from app import create_app

create_app = Flask(__name__)

if __name__ == '__main__':
    
    create_app.run(debug=True)

