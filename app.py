import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///username:password@host:port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return f'<User {self.email}, {self.name}>'

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id for photo
    friend_name = db.Column(db.String(100), nullable=False)
    friend_contact = db.Column(db.String(100), nullable=False)
    upload_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    photo_path = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    activity = db.Column(db.String(100), nullable=True)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # id of the uploader
    def __repr__(self):
        return f'<Photo {self.friend_name}, {self.friend_contact}, {self.photo_path}>'

# TODO: connect to database

# TODO: create database table


# TODO: 

@app.route("/")
def main():
    return render_template('index.html')
