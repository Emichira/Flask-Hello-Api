import unittest
import json
from app import create_app
from app.models import Book, User
from flask import jsonify
import run

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.client = run.create_app.test_client
        self.login={"username":"emmanuel","password":"abc123"}
        self.reset={"email":"emmanuelmichira@gmail.com","password":"123456","confirm_password":"123456"}
        self.user={"username":"collins","email":"emmanuelmichira@gmail.com","password":"123456","confirm_password":"123456"}
        
    def test_api_can_create_user(self):
        """ tests if the api can add a user"""

        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

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

        res=self.client().post('/api/auth/register', data={"username":"chuck","email":"collinsnjau39@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(res.status_code,404)

    def test_api_password_must_be_greater_than_six_characters(self):
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/auth/register', data={"username":"njau","email":"collinsnjau40@gmail.com","password":"123","confirm_password":"123"})
        self.assertEqual(res.status_code,404)

    def test_api_reset_password(self):
        """this will test if user can reset password"""
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/v1/auth/reset-password', data=self.reset)
        self.assertEqual(res.status_code,200)

    def test_api_can_validate_email(self):
        """this will test if user cannot register with an invalid email"""
        result=self.client().post('/api/v1/auth/register',data={"username":"collins","email":"collinsnjaugmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(result.status_code,400)

    def test_api_validate_username(self):
        """this will test if user with empty username will register"""
        result=self.client().post('/api/v1/auth/register',data={"username":" ","email":"collinsnjau@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(result.status_code,400)

    def test_api_validate_password(self):
        """this will test if user with empty password
        can register""" 
        result=self.client().post('/api/v1/auth/register',data={"username":"collins","email":"collinsnjau@gmail.com","password":"       ","confirm_password":"       "})
        self.assertEqual(result.status_code,400)   

    def tearDown(self):
        User.user_list=[]    

if __name__ == "__main__":
    unittest.main()


