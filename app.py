import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///username:password@host:port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TODO: create database
''' (example)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
'''
## TODO: USER TABLE
'''
USER
email, password, name, contact
'''

## TODO: PHOTO TABLE
'''
PHOTO
email, upload_date, photo
'''

# TODO: connect to database

# TODO: create database table


# TODO: 

@app.route("/")
def main():
    return render_template('index.html')
