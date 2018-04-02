import re

class Book(object):
    book = [
        {
            'ISBN': 00001,
            'title': 'MacBeth',
            'author': 'William Shakespear',
            'date_published': '02/02/2018',
            'category': 'History'
        },
        {
            'ISBN': 00002,
            'title': 'Long Walk To Freedom',
            'author': 'Nelson Mandela',
            'date_published': '02/02/2018',
            'category': 'Biography'
        }
    ]
    
    """class to create instance of books"""
    def __init__(self):
        """ list to hold books a user creates """
        self.books_list=[]

    """Adds a new book """
    def add_book(self, ISBN, title, author, date_published, category):
        
        books_dict = {}

        for book in self.books_list:
            if title == book["title"]:
                response = {"message":"Please enter another book name, book name already exists"}
                return response
        
        if len(title) < 2:
            response = {"message":"Input a book name that is atleast 2 characters"}
            return response

        elif not re.match("0?[1-9]|[12][0-9]|3[01])[/ -](0?[1-9]|1[12])[/ -](19[0-9]{2}|[2][0-9][0-9]{2}", date_published):
            response = {"message": "Date published should be in the format DD/MM/YY"}
            return response
        
        elif len(author) > 1:
            books_dict['ISBN'] = str(len(self.books_list) + 1)
            books_dict['title'] = title
            books_dict['author'] = author
            books_dict['category'] = category
            books_dict['date_published'] = date_published

            self.books_list.append(books_dict)

        response = {"message":"Book added successfully"}
        return response

    """Delete a book  """
    def delete(self, ISBN, title):
        for book in self.books_list:
            if title == book["title"]:
                if ISBN == book["ISBN"]:
                    self.books_list.remove(book)
                    response = {"message":"Book deleted successfully"}
                    return response
            else:
                response = {"message":"Unsuccessful, Please delete an available book"}
                return response
        response = {"message":"The book you want to delete cannot be found"}
        return response

    """ Retrieves all books stored in the books list"""
    
    def get_all(self):
        return self.books_list

    """ Get a books by its ISBN ID"""
    def get_single_book(self, ISBN):
        #Check if book exists in books_list
        for book in self.books_list:
            if ISBN == book['ISBN']:
                return book
            else:
                response = {"message":"Book not found. Please search an already created book"}
        return response 


class User(object):
    user = [
        {
            'email': 'abc@abc.com',
            'password': '12345678',
            'role': 'user'
        },
        {
            'email': 'emmanuel@abc.com',
            'password': '87654321',
            'role': 'admin'
        }
        ]
    # return user
    """ User class handles registration and login of users """
    """ user_list will contain a dictionery of created users"""
    
    def __init__(self):
        # self.email = email
        # self.password = password
        # self.role = role
        self.user_list=[]

    def register(self, email, password, confirm_password, role):
        """ Create user accounts by user info to empty dictonary """
        user_dict = {}

        for user in self.user_list:
            if email == user['email']:
                response = {"message":"Account already exists. Please login or Recover account"}
                return response
        if len(password) < 8:
            response = {"message":"Input a password that is at least 6 characters long"}
            return response

        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            response = {"message":"Please a provide a valid email"}
            return response

        elif password == confirm_password:
            user_dict['email'] = email
            user_dict['password'] = password

            self.user_list.append(user_dict)
        else:
            response = {"message":"Password do not match"}
            return response
        response = {"message":"Successfully registered a user account"}
        return response

    def login(self, email, password):
        """ Login user by checking if user exists in
            users_lisr
        """
        for user in self.user_list:
            if email == user['email']:
                if password == user['password']:
                    response = {"message":"You have successfully logged into Hello Library"}
                    return response
                response = {"message":"Password Incorrect"}
                return response
        response = {"message":"User account does not exist, please sign up"}
        return response

    def reset_password(self, new_password, confirm_password):
        for user in self.user_list:
            if new_password == confirm_password:
                user['password'] = new_password
                response = {"message":"Password changed successful"}
                return response
            response = {"message":"Password and confirm password should match"}
            return response
        response = {"message":"User account does not exist, sign up!"} 
        return response

    def check_email_exists(self, email):
        """validates email to avoid two accounts with same user email"""
        for user in self.user_list:
            if user.get("email") == email:
                return True
            
            return False
    
    @staticmethod
    def validate_password(password):
        if len(password)<6:
            return True

        return False

    @staticmethod
    def validate_email(email):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            return True
        return False

    @staticmethod
    def validate_username(username):
        if not re.match(r"^[A-Za-z0-9\.\+_-]*$",username):
            return True
        return False

    @staticmethod
    def validate_password_format(password):
        if not re.match(r"^[A-Za-z0-9\.\+_-]*$",password):
            return True
        return False

class Admin(User):
    
    def __init__(self, email, password, role="admin"):
        super(Admin, self).__init__()
