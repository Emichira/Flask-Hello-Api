import unittest
import json
from app import create_app
from app.models import Book, User
from flask import jsonify
import run

#class to respresent admin testcase
class AdminApiEndpointTestCase(unittest.TestCase):
    
        def setUp(self):
            self.client = run.create_app.test_client
            self.book= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
            self.testbook= {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
        
        def test_api_book_creation(self):
            #test if the api can create a business 
            res=self.client().post('/api/v1/books', data=self.book)
            self.assertEqual(res.status_code,201)
            # self.assertIn("MacBeth",str(res.data))

        def test_api_can_get_all_books(self):
            #tests if the api can get all the books
            res=self.client().post('/api/v1/books', data=self.book)

            self.assertEqual(res.status_code,201)

            result=self.client().get('/api/v1/books')

            self.assertEqual(result.status_code,200)

            # self.assertIn("MacBeth",str(res.data))

        def test_api_can_get_books_by_id(self):
            res=self.client().post('/api/v1/books', data=self.book)
            res.test=self.client().post('/api/v1/books', data=self.testbook)

            self.assertEqual(res.status_code,201)
            #convert response to json
            result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

            #make get request and add the id
            get_request=self.client().get('/api/v1/books/{}'.format(result_in_json['id']))

            #assert the request status
            self.assertEqual(get_request.status_code,200)
        
        def test_api_can_modify_book(self):
    
            #tests if a the api can get a books and edit it 
            res=self.client().post('/api/v1/books', data=self.book)

            self.assertEqual(res.status_code,201)
            #convert response into json so as to get the id
            result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

            #make a put request
            #this edits the current book
            put_request=self.client().put('/api/v1/books/{}'.format(result_in_json['id']), data={"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"})

            self.assertEqual(put_request.status_code,200)

        def test_api_deletes_books(self):
            #test if api can delete a book
            res=self.client().post('/api/v1/books', data=self.book)

            self.assertEqual(res.status_code,201)
            #convert response into json so as to get the id
            result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))
            
            #delete and pass in the id
            result=self.client().delete('/api/v1/books/{}'.format(result_in_json['id']))

            # self.assertEqual(result.status_code,200)
            #try to run get request for deleted business
            deleted_books=self.client().get('/api/v1/books/{}'.format(result_in_json['id']))
            
            #should return 404
            self.assertEqual(deleted_books.status_code,404)

            
if __name__ == "__main__":
    unittest.main()
    #test API can get a single book using its id
    #test API can edit/modify an existing book
    #test API can delete an existing book



    
    
