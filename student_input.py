
import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="school_registrations"
)

print("Database connected successfully!")

# Create cursor
mycursor = mydb.cursor()

# Get student details from user
name = input("Enter student name: ")
student_class = input("Enter class (11th/12th): ")
school = input("Enter school name: ")
phone = input("Enter phone number: ")

# SQL query
sql = """
INSERT INTO students
(student_name, student_class, school_name, phone_number)
VALUES (%s, %s, %s, %s)
"""

values = (name, student_class, school, phone)

# Insert details
mycursor.execute(sql, values)

# Save data
mydb.commit()

print("\nRegistration successful!")
print("Welcome", name)

# Close connection
mycursor.close()
mydb.close()
