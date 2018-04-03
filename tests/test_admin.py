import unittest
import json
from app import app
from app.models import Book, User
from flask import jsonify

#class to respresent admin testcase
class AdminApiEndpointTestCase(unittest.TestCase):
    
        def setUp(self):
            #get the app test client
            self.client = app.test_client
                                #data to use
            self.book= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
            self.testbook= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
            self.book = Book()
        

        def tearDown(self):
            del self.book
       
if __name__ == "__main__":
    unittest.main()




    
    
