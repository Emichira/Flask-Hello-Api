import unittest
import os
import json
from app import create_app
from app.models import Book
from flask import jsonify

#class to respresent admin testcase
class AdminApiEndpointTestCase(unittest.TestCase):
    
        def setUp(self):
            self.app=create_app(config_name="testing")
                    #get the app test client
            self.client = self.app.test_client
                    #data to use
            self.book= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
            self.testbook= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}




    
    
