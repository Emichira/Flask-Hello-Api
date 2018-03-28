import unittest, app
from app.models import Book, User
import json
from app import create_app
from flask import jsonify
import run

class BookCreation(unittest.TestCase):
    
    def setUp(self):
        self.client = run.create-app.test_client
        self.book = {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018","category": "Good Reads"}

    def tearDown(self):
        """clears list after every test"""
        Book.books_list=[] 

if __name__ == "__main__":
    unittest.main()     