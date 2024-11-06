from db import insert_data_into_users, get_user_details, add_or_delete_details_of_user
from datetime import datetime

def get_valid_date():
    while True:
        dob = input("Enter a Date  (YYYY-MM-DD): ")
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            return dob
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")

def record_operations(user_name):
    while True:
        print("Welcome to Ledger App...! \nNow you can Add your Credit, Debit history here")
        print("<<<<<<    1. Add Credited / Debited History    >>>>>>")
        print("<<<<<<<   2. Show Statements and Balance ")
        print("<<<<<<    2. Delete history    >>>>>>")
        print("<<<<<<    4. Log Out    >>>>>>")
        select2 = input("Please select a option from Above : ")
        if select2 == "1":
            date = get_valid_date()
            particular = input("Details of transaction : ")
            amount = int(input("Enter amount Credit(+) / Debit(-) ex : Credit = 120, Debited = - 120 : "))
            add_or_delete_details_of_user(date, particular, amount, user_name)
        elif select2 == "2":
            pass
        elif select2 == "3":
            pass
        elif select2 == "4":
            return False
        else:
            print("<<<<<<<<<<   You enter a inappropreate option. Try Again. >>>>>>>>>>>>>>")
        # add_or_delete_details_of_user(select2)

def operations(select) :
    while True:
        if select == "1":
            print("Welcome")
            user_name = input("Enter your User Name: ")
            password = input("Enter your Password: ")

            if get_user_details(user_name, password):
                print("Login successful! Welcome back.")
                record_operations(user_name)
                return True
            else:
                print("Login failed. Please check your username and password.")
                return True
        elif select == "2":
                name = input("Enter your Name: ")
                phone_number = input("Enter your Phone number: ")
                dob = get_valid_date()
                user_name = input("Enter your User Name: ")
                password = input("Enter your Password: ")
                insert_data_into_users(name, phone_number, dob, user_name, password)
                record_operations(user_name)
                return True  
        elif select == "3":
            return False
        else:
            print("Please select a valid option.")
            return True
