from flaskdemo import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Student({self.fullname} - {self.fullname})"
