from user import User 

users = {}

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = User(username,password)
    print("User registered successfully")