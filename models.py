import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from config import Config
from forms import LoginForm, RegisterForm, UploadPhotoForm

app = Flask(__name__)
#create instance of Flask class
#predefined variable, name of module (app)

#configuring app to use SQLite database using SQL alchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = Config.SECRET_KEY
#This line sets the Flask application's secret key to a value specified in Config.

db = SQLAlchemy(app)
#initializes an instance of the SQLAlchemy class with the Flask application (app).

# Database models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(30), nullable=False)
    #defines a string representation of a User object.
    def __repr__(self):
        return f'<User {self.email}, {self.name}>'

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id for photo
    friend_name = db.Column(db.String(100), nullable=False)
    friend_contact = db.Column(db.String(100), nullable=False)
    upload_date = db.Column(db.DateTime(timezone=True), server_default=func.now()) #gets current timestamp
    photo_path = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    activity = db.Column(db.String(100), nullable=True)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # id of the uploader, references the id column of the user table
    def __repr__(self):
        return f'<Photo {self.friend_name}, {self.friend_contact}, {self.photo_path}>'


def create_new_db():
    db.drop_all()  # clear database
    db.create_all()
    #clears existing database tables, recreates tables based on defined models
    
def db_add_user(name, email, password, contact): #adds new user to the database

#creates new user
    user = User(name=name,
                email=email,
                password=password,
                contact=contact)
    db.session.add(user) #adds to current session
    db.session.commit() #commits the session to save its changes to the database

#adds a new photo to database, adding to current session and committing
def db_upload_photos(friend_name, friend_contact, photo_path, contact, uploader_id):
    photo = Photo(friend_name='John',
                  friend_contact='0987654321',
                  photo_path='photo.jpg',
                  contact='0987654321',
                  uploader_id=1)
    db.session.add(photo)
    db.session.commit()

#example of using these functions
def populating_example_data():
    db_add_user('John',
                'johndoe@example.com',
                'password',
                '0987654321')
    db_upload_photos('John',
                    '0987654321',
                    'photo.jpg',
                    '0987654321',
                    1)

with app.app_context():
    create_new_db() #creates a new database
    populating_example_data() #populates the database with the example data
    
#this is like what's in app/routes.py (usually in a separate file)
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/upload")
def upload():
    upload_form = UploadPhotoForm()
    return render_template('upload.html', title='Upload', form=upload_form)
    
    #render template takes in the data passed to it, renders it to the template


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('upload'))
    if request.method == 'GET':
        login_form = LoginForm()
        return render_template('login.html', title='Sign In', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        register_form = RegisterForm()
        return render_template('register.html', title='Register', form=register_form)
    if request.method == 'POST':
        register_form = RegisterForm()
        db_add_user(register_form.name.data, register_form.email.data, register_form.password.data, register_form.contact.data)

if __name__ == '__main__':
    app.run()
