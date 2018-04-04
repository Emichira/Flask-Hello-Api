import unittest
import json
import os, sys
sys.path.append("..")
from app import app
from app.models import Book, User
from flask import jsonify, Flask
import flask_testing

#class to respresent admin testcase
class AdminApiEndpointTestCase(unittest.TestCase):
    
        def setUp(self):
            # get the app test client
            self.client = app.test_client()
            #data to use
            self.book= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
            self.testbook= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
            self.book = Book()

        def test_delete(self):
            # ISBN has not been provided
            # print(self.book.delete("", "MacBeth"))
            assert("You must specify ISBN number" in str(self.book.delete("", "MacBeth")))

            # Title has not been provided 
            # print(self.book.delete(ISBN="0001"))
            assert("You must specify Title" in str(self.book.delete(ISBN="0001")))

            #Test suceesful delete
            #Retrieve a valid book title
            books_list = self.book.books_list
            title = books_list[0]["title"]
            ISBN = books_list[0]["ISBN"]

            print(title)
            if title is not None:
                assert("Book deleted successfully" in str(self.book.delete(ISBN, title)))

            # Unsuccessful delete
            title = "stsUnsuccessful, Please delete an available booksfdsfds334432423"
            ISBN = 1232564565465465465465465465465654
            assert("Unsuccessful, Please delete an available book" in str(self.book.delete(ISBN, title)))

        def test_get_single_book(self):
            # ISBN not passed
            assert("Book not found. Please search an already created book" in str(self.book.get_single_book(ISBN="0001")))

            # Book found
            book = self.book.books_list[0]
            ISBN = book["ISBN"]

            if book is not None:
                self.assertEquals(book, self.book.get_single_book(ISBN))    
        
        def test_add_book(self):
            # Test all information is provided
            self.assertEquals("Please input ISBN, title, author, date and category", self.book.add_book())
            
            # Check for a valid book title
            title = "i"
            assert("Input a book name that is atleast 2 characters" in str(self.book.add_book("i", title, "manu", 2018/02/28, "Good Reads")))

            # Check for a valid author
            author = "m"
            assert("Please input an author name with at least 2 character" in self.book.add_book("df", "Game of thrones", author, 2018/02/02, "Good Reads"))                       
            
        def test_api_add_book(self):
            book = self.book.books_list[0]
            ISBN = book["ISBN"]       

            response = self.client.get('/api/v1/books', content_type='application/json')
            print(response.data)
            self.assertEquals(response.status, '200 OK')
            assert(str(ISBN) in response.data)

            new_book = {
                "ISBN": "0001",
                "title": "MacBeth",
                "author": "Shakespear",
                "date-published": "2018/02/02",
                "category": "Good Reads"
                }
            response = self.client.post('/api/v1/books',
                data=json.dumps(new_book), content_type='application/json')
            self.assertEquals(response.status_code, 201)

        def tearDown(self):
            del self.book

if __name__ == "__main__":
    unittest.main()




    
    
