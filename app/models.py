import re

class Book(object):
    """class to create instance of books"""
    def __init__(self, ISBN, title, author, date_published, category):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.date_published = date_published
        self.category = category
        self.books_list=[]

        #add a new book
    def put(self, ISBN, title, author, date_published, category):
        
        books_dict = {}

        for book in self.books_list:
            if title == book["title"]:
                response = {"message":"Please enter another book name, book name already exists"}
                return response
        
        if len(title) < 2:
            response = {"message":"Input a book name that is atleast 2 characters"}
            return response

        elif re.match("0?[1-9]|[12][0-9]|3[01])[/ -](0?[1-9]|1[12])[/ -](19[0-9]{2}|[2][0-9][0-9]{2}", date_published):
            books_dict['ISBN'] = str(len(self.books_list) + 1)
            books_dict['title'] = title
            books_dict['author'] = author
            books_dict['category'] = category
            books_dict['date_published'] = date_published

            self.books_list.append(books_dict)

        response = {"message":"Book added successfully"}
        return response

        #delete a book  
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

        #retrieves all books stored in the books list
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
    
    """ user_list will contain a dictionery of created users"""
    user_list=[]
    
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

        self.users = {}

    def save_user(self,email,password):
        """
        this method gets user details as parameters,
        uses them to create a dict and append dict
        to the user_list
        """
        new_user={}

        new_user["email"]=email
        new_user["password"]=password

        if new_user["password"] == new_user["password"]:
            User.user_list.append(new_user)
            
            message="successfully registered user"
            return message

        
        message="Invalid password, sign upto create an account"
        return message

    @classmethod
    def login(cls,email,password):
        """logs in user by checking if they exist in the list"""
        for user in cls.user_list:
            if user["email"]==email and user["password"]==password:
                message="you have successfully logged in"
                return message
            
            message="email or email is invalid"
            return message  

    @classmethod
    def check_email_exists(cls,email):
        """validates email to avoid two accounts with same user email"""
        for user in cls.user_list:
            if user.get("email") == email:
                return True
            
            return False
    
    @staticmethod
    def validate_password(password):
        if len(password)<6:
            return True

        return False

    @staticmethod
    def reset_password(email,password,confirm_password):
        for user in User.user_list:
            if user["email"] == email:
                if password == confirm_password:
                    user["password"]=password
                    user["confirm_password"]=confirm_password
                    message="Password reset was successful"
                    return message

                else:
                    message="Password and confirm password must be the same"
                    return message
            else:
                message="Account does not exist"
                return message
    
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
