import psycopg2
from psycopg2 import sql

class DB:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def open_connection(self):
        """Open a connection to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Database connection opened successfully.")
        except Exception as e:
            print("Failed to open database connection:", e)

    def create_employee_table(self):
        """Create the employee table if it doesn't exist."""
        if not self.connection:
            print("No open connection. Call open_connection first.")
            return

        try:
            cursor = self.connection.cursor()
            create_table_query = """
                CREATE TABLE IF NOT EXISTS employee (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INTEGER NOT NULL,
                    address VARCHAR(255),
                    salary NUMERIC(10, 2),
                    height NUMERIC(5, 2),
                    weight NUMERIC(5, 2)
                )
            """
            cursor.execute(create_table_query)
            self.connection.commit()
            print("Employee table created or already exists.")
        except Exception as e:
            self.connection.rollback()
            print("Failed to create employee table:", e)
        finally:
            cursor.close()

    def insert_registration(self, name, age, address, salary, height, weight):
        """Insert registration details into the database table."""
        if not self.connection:
            print("No open connection. Call open_connection first.")
            return

        try:
            cursor = self.connection.cursor()
            insert_query = sql.SQL("""
                INSERT INTO employee (name, age, address, salary, height, weight)
                VALUES (%s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (name, age, address, salary, height, weight))
            self.connection.commit()
            print("Registration details inserted successfully.")
        except Exception as e:
            self.connection.rollback()
            print("Failed to insert registration details:", e)
        finally:
            cursor.close()

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


