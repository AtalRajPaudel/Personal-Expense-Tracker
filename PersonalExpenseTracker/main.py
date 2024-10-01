from user import User 

users = {}

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = User(username,password) ##Here value is stored in the dictionary with the key being the username and value being the object
    print("User registered successfully")
