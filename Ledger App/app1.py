from app_operations import operations
# from datetime import datetime

a = True
while a :
    print("Welcome to the Ledger Application")
    print("1. Log in")
    print("2. Register")
    print("3. Exit")
    select = input("Please select an option from above (1/2/3): ")

    a = operations(select)

print("Thank You...! Visit Again")