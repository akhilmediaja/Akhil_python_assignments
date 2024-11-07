from db import DB
db = DB(dbname="oops01", user="postgres", password="akhil")
db.open_connection()


db.create_employee_table()


db.insert_registration(name="John Doe", age=30, address="123 Main St", salary=50000, height=175, weight=70)

db.close_connection()