import unittest
import json
import os, sys
sys.path.append("..")
from app import app
from app.models import Book, User
from flask import jsonify
import run

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
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

    def test_home_route(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.client.get('/') 

        # assert the response data
        self.assertEqual(result.status_code,200, {'Message': 'Welcome to Hello Library'})
    
    def test_if_user_is_registered(self):
    
        self.user.user_list = [{'email': 'abc@abc.com', 'password': 'gddgdg5'}]
        msg = self.user.login("abc@abc", "gddgdg5")
        self.assertEqual(msg, {"message":"User account does not exist, Register account"})
        
    def test_register(self):
        # Test if user can successfully registered a user account
        msg = self.user.register("mich@anuel.com", "wertrWER4", "wertrWER4", "role=user")
        self.assertEqual(msg, {"message":"Successfully registered a user account"})

    def test_cannot_create_account_with_email_already_exist(self):
        
        self.user.register("bruh@bruh.com", "wertrWER4", "wertrWER4", "role=user")
        msg = self.user.register("bruh@bruh.com", "asdQWER4", "asdQWER4", "role=user")
        self.assertEqual({"message":"Account already exists"}, msg)

    def test_api_password_must_be_greater_than_six_characters(self):

        msg = self.user.register("emmanuel@abc.com", "test", "test","role=user")
        self.assertEqual(msg, {"message":"Input a password that is at least 6 characters long"})

    def test_reset_password(self):
        """this will test if user can reset password"""

        msg = self.user.register("emmanuel@abc.com", "djgjdbk432", "sgdsghds95", "role=admin")
        self.assertEqual(msg, {"message":"Password do not match"})  

    def test_api_can_validate_email(self):
        """this will test if user cannot register with an invalid email address"""
        msg = self.user.register("emmanuel@abc.sfd@&com", "djgjdbk432", "sgdsghds95", "role=admin")
        self.assertEqual(msg, {"message":"Please a provide a valid email"})

    def test_api_validate_email_address(self):
        """this will test if user with empty username will register"""
        msg = self.user.register("", "djgjdbk432", "sgdsghds95", "role=admin")
        self.assertEqual(msg, {"message":"Please a provide a valid email"})

    def test_user_is_able_to_register(self):
        """Test that user is able to register
        ensure that a valid post request to /api/v1/auth/register 
        registers a user
        """
        new_user = {
            "email": "abc@abc.com30",
            "password": "123456789030",
            "confirm_password": "123456307890",
            "role": "admin"
            }
        response = self.client.post("/api/v1/auth/register", data=json.dumps(new_user), content_type="application/json")
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        """Tests that user is able to login"""
        new_user = {"email": "abc@abc.com", "password": "1234567890"}

        response = self.client.post('/api/v1/auth/login', data=json.dumps(new_user), content_type='application/json')
        self.assertEquals(response.status_code, 200)

    def test_len_password_register(self):
        """Test if password length is more than 8 characters"""
        new_user = {
            "email": "abc@abc.com",
            "password": "",
            "confirm_password": "1234567890",
            "role": "admin"
            }

        response = self.client.post('/api/v1/auth/register', data=json.dumps(new_user), content_type='application/json')
        # self.assertEquals(response.status_code, 200)
        self.assertIn("Passwords should match", str(response.data))

    def test_password_match_register(self):
        """Tests if password and confirmation password match"""
        new_user = {
            "email": "abc@abc.com",
            "password": "1234567890",
            "confirm_password": "10",
            "role": "admin"
            }

        response = self.client.post('/api/v1/auth/register', data=json.dumps(new_user), content_type='application/json')
        self.assertIn("Passwords should match", str(response.data))

    def test_role_register(self):
        """Tests if user has defined a role"""
        new_user = {
            "email": "abc@abc.com",
            "password": "1234567890",
            "confirm_password": "1234567890",
            "role": ""
            }
        response = self.client.post('/api/v1/auth/register', data=json.dumps(new_user), content_type='application/json')
        self.assertIn("Fill in  your role to register", str(response.data))

    def test_api_reset_password(self):
        new_user = {"email": "abc@abc.com", "new_password": "123450", "confirm_password": "1234567890"}

        response = self.client.post('/api/v1/auth/reset-password', data=json.dumps(new_user), content_type='application/json')
        self.assertIn("Password and confirm password should match", str(response.data))

        
    
    def tearDown(self):
        """ Teardown Users Class test case  """
        del self.user

if __name__ == "__main__":
    unittest.main()