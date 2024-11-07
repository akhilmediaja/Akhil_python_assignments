# db_operations.py
import psycopg2

class DB:
    def __init__(self, db_name="your_database", user="your_user", password="your_password", host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS records (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER,
            city VARCHAR(50)
        )
        '''
        self.cursor.execute(query)
        self.connection.commit()
        print("Table created successfully.")
    
    def insert_value(self, name, age, city):
        query = "INSERT INTO records (name, age, city) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, age, city))
        self.connection.commit()
        print("Value inserted successfully.")
    
    def update_value(self, record_id, name=None, age=None, city=None):
        if name:
            self.cursor.execute("UPDATE records SET name = %s WHERE id = %s", (name, record_id))
        if age:
            self.cursor.execute("UPDATE records SET age = %s WHERE id = %s", (age, record_id))
        if city:
            self.cursor.execute("UPDATE records SET city = %s WHERE id = %s", (city, record_id))
        self.connection.commit()
        print("Value updated successfully.")
    
    def delete_value(self, record_id):
        query = "DELETE FROM records WHERE id = %s"
        self.cursor.execute(query, (record_id,))
        self.connection.commit()
        print("Value deleted successfully.")
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")
