
import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root",
    database="school_registrations"
)

print("Database connected successfully!")

# Create cursor
mycursor = mydb.cursor()

# Student details
name = "Rahul"
student_class = "11th"
school = "Government PU College"
phone = "9876543210"

# Insert student details
sql = """
INSERT INTO students
(student_name, student_class, school_name, phone_number)
VALUES (%s, %s, %s, %s)
"""

values = (name, student_class, school, phone)

mycursor.execute(sql, values)

# Save the record
mydb.commit()

print("Student registered successfully!")

# Close connection
mycursor.close()
mydb.close()
