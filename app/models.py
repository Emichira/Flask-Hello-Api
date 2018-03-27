import re

class Book(object):
    """class to create instance of books"""
    books_list=[]

    def __init__(self, ISBN, title, author, date_published, category):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.date_published = date_published

        self.books = {}

    # def add_a_book(self, ISBN, title, author, date_published, category):

    #     books_list = []

    #     books_list["category"]= category
    #     books_list["title"]= title
    #     books_list["author"]= author
    #     books_list["date_published"]=date_published
    #     books_list["ISBN"]=ISBN


    #     Book.books_list.append(books_list)
    #     return books_list

        #add a book or modify a book
    def put(self, title, author, ISBN):
        
        book = {title:author}
        self.books[ISBN] = book
		
        return (self.books[ISBN])

        #delete a book  
    def delete(self, ISBN):
   
        del self.books[ISBN]
        
        return (self.books)

        #retrieve all books
    def get_all(self):
        return self.books


    def get_single_book(self, ISBN):
    	return (self.books[ISBN])


class User(object):
    
    """ user_list will contain a dictionery of created users"""
    user_list=[]
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.users = []

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
