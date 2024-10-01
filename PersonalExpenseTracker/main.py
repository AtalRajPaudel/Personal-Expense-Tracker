from user import User 
from expense import Expense
import json

users = {}

def register_user():
    username = input("Enter username: ")
    if username in users:
        print("Username already taken. Please choose a different username.")
        return 0
    password = input("Enter password: ")
    users[username] = User(username,password)
    print("User registered successfully")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username].password == password:
        print("Login successful.")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return None




expenses = [] ## Initialize a list to hold expenses

def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD) : ")
    expense = Expense(amount,category,date)
    expenses.append(expense)
    print("Expense added successfully. ")

def view_expense():
    print("Expenses:  ")
    for expense in expenses: ## To loop through each expense in the list
        print(expense) 
        ## calls the __str__ method of the Expense class. and prints as the format 



def save_expenses():
    with open('project/PersonalExpenseTracker/data.json','w') as f:
        json.dump([expense.__dict__ for expense in expenses],f)

def load_expenses():
    global expenses # Use the global expenses list
    try: 
        with open('project/PersonalExpenseTracker/data.json','r') as f:
            expenses = [Expense(**item) for item in json.load(f)]
    except FileNotFoundError:
        expenses = []
    except Exception as e:
        print(f"An error occured. : {e}")


def main():
    load_expenses()
    while True:
        choice = input("1. Register \n2.Login \n3.Add Expense \n4.View Expenses\n5.Exit \n Choose an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            user = login_user()
            if user:
                break
        elif choice == '3':
            add_expense()
        elif choice == '4':
            view_expense()
        elif choice == '5':
            save_expenses() ## To save expense (like in the cloud) before exiting
            exit()

main()
