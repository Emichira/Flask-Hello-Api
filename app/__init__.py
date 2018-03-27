import os
from flask import Flask, render_template, request
from flask_api import FlaskAPI
from flask import request, jsonify, abort,session
from models import User, Book


create_app = Flask(__name__, instance_relative_config=True)

from app import views
