import psycopg2
from datetime import datetime
# from secrets import 
# from secrets import get_db_secrets

def insert_data_into_users(name, phone_number, dob, user_name, password):
    try:
        dob_obj = datetime.strptime(dob, "%Y-%m-%d")
        # bd_details = get_db_secrets()
        with psycopg2.connect(host="localhost", user="postgres", password="akhil", port=5432, dbname="db2") as con:
            with con.cursor() as cur:
                query = "INSERT INTO users (name, phone_number, dob, user_name, password) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(query, (name[:20], phone_number, dob_obj, user_name[:20], password[:20]))
                con.commit()
                print("User data inserted successfully.")
    except Exception as err:
        print("Error inserting data:", err)

def get_user_details(user_name, password):
    try:
        with psycopg2.connect(host="localhost", user="postgres", password="akhil", port=5432, dbname="db2") as con:
            with con.cursor() as cur:
                query = "SELECT * FROM users WHERE user_name = %s AND password = %s"
                cur.execute(query, (user_name, password))
                user = cur.fetchone()
                return bool(user)
    except Exception as err:
        print("User or password incorrect:", err)
        return False

def add_or_delete_details_of_user(date, particular, amount, user_name):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        with psycopg2.connect(host="localhost", user="postgres", password="akhil", port=5432, dbname="db2") as con:
            with con.cursor() as cur:
                query = "INSERT INTO statements (date, particular, amount, user_name) VALUES (%s, %s, %s, %s)"
                cur.execute(query, (date, particular[:20], amount, user_name[:20]))
                con.commit()
                print("Transaction data inserted successfully!")
    except Exception as err:
        print("Error inserting data:", err)
    finally:
        cur.close()
        con.close()
         