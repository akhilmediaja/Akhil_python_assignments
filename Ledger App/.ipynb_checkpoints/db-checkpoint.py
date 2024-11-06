import psycopg2

connection = psycopg2.connect(host = "localhost", user = "postgres", password = "akhil", port = 5432, dbname = "ledgerDB")