def get_db_secrets():
    return {"host":"localhost", "user":"postgres", "password":"akhil", "port":5432, "dbname":"db2"}


bd_details = get_db_secrets()

for i in bd_details:
    print(bd_details.get(i))