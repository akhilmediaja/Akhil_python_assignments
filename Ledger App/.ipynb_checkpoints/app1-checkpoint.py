print("Wel Come to Ledger Application")
print("1. Log in")
print("2. Register")
select = input("Please select a option from above 1 / 2 : ")
if select == "2":
    name = input("Enter your Name : ")
    phone_number = input("Enter your Phone number : ")
    DOB = input("Enter your DOB : ")
    user_name = input("Enter your User Name : ")
    password = input("Enter your Password : ")
elif select == "1":
    user_name = input("Enter your User Name : ")
    Password = input("Enter your Password : ")
else:
    print("Please select from above options")