
from flask import Flask, render_template, request
import mysql.connector
from openpyxl import Workbook, load_workbook
import os

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root",
        database="school_registrations"
    )


def save_to_excel(student_name, father_name, mobile,
                  class_name, school_name, competition):

    file_name = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "student_registrations.xlsx"
    )

    if os.path.exists(file_name):
        workbook = load_workbook(file_name)
        sheet = workbook.active
    else:
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Student Registrations"

        sheet.append([
            "Student Name", "Father Name", "Mobile",
            "Class", "School Name", "Competition"
        ])

    sheet.append([
        student_name, father_name, mobile,
        class_name, school_name, competition
    ])

    workbook.save(file_name)
    print("Student saved in Excel!")
    print("Excel location:", file_name)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    try:
        student_name = request.form["student_name"]
        father_name = request.form["father_name"]
        mobile = request.form["mobile"]
        class_name = request.form["class_name"]
        school_name = request.form["school_name"]
        competition = request.form["competition"]

        mydb = get_connection()
        mycursor = mydb.cursor()

        sql = """
        INSERT INTO studentss
        (student_name, father_name, mobile, class_name,
         school_name, competition)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            student_name, father_name, mobile,
            class_name, school_name, competition
        )

        mycursor.execute(sql, values)
        mydb.commit()

        print("Student saved in MySQL!")

        mycursor.close()
        mydb.close()

        save_to_excel(
            student_name, father_name, mobile,
            class_name, school_name, competition
        )

        return "Registration successful! Saved in MySQL and Excel."

    except Exception as e:
        print("Error:", e)
        return f"Registration failed: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
