
from app import User, create_app, Book
from app import reset_password, login, register, logout, add_book
from flask import Flask

create_app = Flask(__name__)

create_app.add_url_rule(
    '/api/v1/auth/register', view_func=register.as_view(
        'register'), methods=['GET', 'POST'])
create_app.add_url_rule(
    '/api/v1/auth/login', view_func=login.as_view(
        'login'), methods=['GET', 'POST'])
create_app.add_url_rule(
    '/api/v1/books', view_func=add_book.as_view(
        'books'), methods=['GET', 'POST'])
create_app.add_url_rule(
    '/api/v1/auth/logout', view_func=logout.as_view(
        'logout'), methods=['POST'])

create_app.add_url_rule(
    '/api/v1/auth/reset-password', view_func=reset_password.as_view(
        'reset-password '), methods=['POST'])

if __name__ == '__main__':
    
    create_app.run()

