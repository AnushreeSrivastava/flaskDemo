from flask import url_for, request, jsonify
from flaskdemo import app
from flaskdemo.models import Student
from flaskdemo import db


@app.route("/")
@app.route("/home")
def home():
    all_students = Student.query.all()
    students = []

    for student in all_students:
        students.append({"fullname": student.fullname, "major": student.major})
    return jsonify({"students": students})


@app.route("/save_new", methods=["POST"])
def save_students():
    student_data = request.get_json()
    new_student = Student(
        fullname=student_data["fullname"], major=student_data["major"]
    )
    db.session.add(new_student)
    db.session.commit()
    return "Done", 201
