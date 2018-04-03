import unittest
import json
from app import app
from app.models import Book, User
from flask import jsonify
import run

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client
        self.login={"username":"emmanuel","password":"abc123"}
        self.reset={"email":"emmanuelmichira@gmail.com","password":"123456","confirm_password":"123456"}
        self.user={"email":"emmanuelmichira@gmail.com","password":"123456","role":"admin"}
        self.user = {
            'email': 'abc@abc.com',
            'password': '12345678',
            'role': 'user'
        }
        self.user = User()
        self.book = Book()

    def test_homepage(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.client().get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_home_route(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.client().get('/') 

        # assert the response data
        self.assertEqual(result.status_code,200, {'Message': 'Welcome to Hello Library'})
    
        """ Checking if the user has an account """
    def test_if_user_is_registered(self):

        self.user.user_list = [{'email': 'abc@abc.com', 'password': 'gddgdg5'}]
        msg = self.user.login("abc@abc", "gddgdg5")
        self.assertEqual(msg, {"message":"User account does not exist, please sign up"})
        
    def test_register(self):
        # """ tests if the api can add a user"""

        result=self.client().post('/api/v1/auth/register', data=self.user, content_type='application/json')
        self.assertEqual(result.status_code,201)

    def test_delete(self):
        book = {"ISBN": "00002", "title":
                "Introduction to programming"}
        response = self.client().delete(
            "/api/v1/books/ISBN", data=book,
            content_type="application/json")
        self.assertEqual(response.status_code, 204)

    def test_api_can_login_user(self):
        """user creates account"""
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        """user logs in"""
        res=self.client().post('/api/v1/auth/login', data=self.login)
        self.assertEqual(res.status_code,200)

    def test_cannot_create_account_with_email_already_exist(self):
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/auth/register', data={"email":"abc@abc.com","password":"12345678","confirm_password":"12345678"})
        # self.assertEqual(res.status_code,404)

    def test_api_password_must_be_greater_than_six_characters(self):
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/auth/register', data={"email":"abc@abc.com","password":"123","confirm_password":"123"})
        # self.assertEqual(res.status_code,404)

    def test_api_reset_password(self):
        """this will test if user can reset password"""
        result=self.client().post('/api/v1/auth/register', data=self.user)
        # self.assertEqual(result.status_code,200)

        res=self.client().post('/api/v1/auth/reset-password', data=self.reset)
        # self.assertEqual(res.status_code,200)

    def test_api_can_validate_email(self):
        """this will test if user cannot register with an invalid email"""
        result=self.client().post('/api/v1/auth/register',data={"email":"abc\`abc.com","password":"12345678","confirm_password":"12345678"})
        # self.assertEqual(result.status_code,400)

    def test_api_validate_username(self):
        """this will test if user with empty username will register"""
        result=self.client().post('/api/v1/auth/register',data={"email":"abc@abccom","password":"12345678","confirm_password":"12345678"})
        # self.assertEqual(result.status_code,400)

    def test_api_validate_password(self):
        """this will test if user with empty password
        can register""" 
        result=self.client().post('/api/v1/auth/register',data={"email":"abc@abc.com","password":"confirm_password"})
        # self.assertEqual(result.status_code,400)     

    def tearDown(self):
        """ Teardown Users Class test case  """
        del self.user

if __name__ == "__main__":
    unittest.main()


