from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:password123@localhost:3306/students"
db = SQLAlchemy(app)

from flaskdemo import routes
