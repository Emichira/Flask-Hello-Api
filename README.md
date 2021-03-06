# Hello~Library

Hello-Books is a simple application that helps manage a library and its processes like stocking, tracking and renting books. With this application users are able to find and rent books using RESTful API's. The application also has an admin section where the admin add books, delete books, increase the quantity of a book etc using RESTful API's.

## Code Integration and Testing

[![Build Status](https://travis-ci.org/Emichira/Flask-Hello-Api.svg?branch=api)](https://travis-ci.org/Emichira/Flask-Hello-Api)
[![Maintainability](https://api.codeclimate.com/v1/badges/bfc582da0c7725676599/maintainability)](https://codeclimate.com/github/Emichira/Flask-Hello-Api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Emichira/Flask-Hello-Api/badge.svg)](https://coveralls.io/github/Emichira/Flask-Hello-Api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/189eb2e03d0540ae95a1c1cf732ebf39)](https://www.codacy.com/app/Emichira/Flask-Hello-Api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Emichira/Flask-Hello-Api&amp;utm_campaign=Badge_Grade)

## Endpoints

 Endpoint                                  |Functionality                    |
|------------------------------------------|---------------------------------|
 POST  /api/books                          | add a book                      |
 PUT /api/books/<bookId>                   | modify a book’s information     |
 DELETE /api//books/<bookId>               | Remove a book                   |
 GET  /api/books                           | Retrieves all books             |
 GET  /api/books/<bookId>                  | Get a book                      |
 POST  /api/users/books/<bookId>           | Borrow a book                   |
 POST /api/auth/register                   | Creates a user account          |
 POST /api/auth/login                      | Logs in a user                  |
 POST /api/auth/logout                     | Logs out a user                 |
 POST /api/auth/reset-password             | Password reset                  |

## Installation & Setup

1. Download & Install Python
 	* Head over to the [Python Downloads](https://www.python.org/downloads/) Site and download a version compatible with your operating system
 	* To confirm that you have successfully installed Python:
		* Open the Command Prompt on Windows or Terminal on Mac/Linux
		* Type python
		* If the Python installation was successfull you the Python version will be printed on your screen and the python REPL will start
2. Clone the repository to your personal computer to any folder
 	* On GitHub, go to the main page of the repository [Flask-Hello-Api](https://github.com/Emichira/Flask-Hello-Api.git)
 	* On your right, click the green button 'Clone or download'
 	* Copy the URL
 	* Enter the terminal on Mac/Linux or Git Bash on Windows
 	* Type `git clone ` and paste the URL you copied from GitHub [https://github.com/Emichira/Flask-Hello-Api.git]
 	* Press *Enter* to complete the cloning process
3. Virtual Environment Installation
 	* Install the virtual environment by typing: `pip install virtualenv` on your terminal
4. Create a virtual environment by running `virtualenv --python python venv`. This will create the virtual environment in which you can run the project.
5. Activate the virtual environment by running `source venv/bin/activate`
6. Enter the project directory by running `cd flask-helo-api`
7. Once inside the directory install the required modules
 	* Run `pip install -r requirements.txt`
8. Inside the application folder run the run.py file:
 * On the terminal type `python run.py` to start the application

## Testing
To run the tests for the app, run;

* nosetests -v


## Authors

* **Emmanuel Michira**

## License

This project is licensed under the MIT License