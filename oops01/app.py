
from db import DB

db = DB(db_name="oops01", user="postgres", password="akhil", host="localhost", port="5432")

while True:
    print("1. Create Tables")
    print("2. Insert Values")
    print("3. Update Values")
    print("4. Delete values")
    print("5. Close Connection")
    print("6. Exit")
    option = input("Select a option from above")

    if option == "1":
        db.create_table()
    elif option == "2":
        db.insert_value("Alice", 25, "New York")
        db.insert_value("Bob", 30, "Los Angeles")
        db.insert_value("Charlie", 35, "Chicago")
    elif option == "3":
        db.update_value(1, age=26)
    elif option == "4":
        db.delete_value(2)
    elif option == "5":
        db.close_connection()
    elif option == "6":
        break
    else:
        print("Select a proper option")










