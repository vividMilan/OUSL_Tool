import mysql.connector
import os
# DB Credentials


def connect_to_database():
    return mysql.connector.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_user"),
        password=os.getenv('db_password'),
        database=os.getenv("db_database")
    )