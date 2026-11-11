
from openpyxl import Workbook
import os

file_name = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "student_registrations.xlsx"
)

workbook = Workbook()
sheet = workbook.active

sheet.title = "Student Registrations"

sheet.append([
    "Student Name",
    "Father Name",
    "Mobile",
    "Class",
    "School Name",
    "Competition"
])

sheet.append([
    "Rahul",
    "Ramesh",
    "9876543210",
    "11th",
    "Government School",
    "Drawing"
])

workbook.save(file_name)

print("Excel file created successfully!")
print("File location:", file_name)
