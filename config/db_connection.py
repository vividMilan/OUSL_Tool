import mysql.connector

# DB Credentials
host="localhost"
user="root"
password="Ilsm@1000"
database="ousl"

def connect_to_database():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )