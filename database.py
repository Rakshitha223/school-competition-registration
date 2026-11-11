

import mysql.connector

# Connect Python to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="school_competition"
)

if mydb.is_connected():
    print("MySQL connected successfully!")

mydb.close()
