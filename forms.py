from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileRequired, FileAllowed

PASSWORD_MIN_LEN = 12
PASSWORD_MAX_LEN = 100

class RegisterForm(FlaskForm):
    # the validators in the field add special modifiers to those fields
    # # without these validators successfully completing and not raising
    # # any errors
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[
                                                Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN),
                                                EqualTo('confirm_password',
                                                message='Passwords must match')
                                                ])
    confirm_password = PasswordField(label='Confirm Password', validators=[Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN)])
    submit = SubmitField('Sign In')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[
                                                Length(min=PASSWORD_MIN_LEN, max=PASSWORD_MAX_LEN),
                                                ])
    submit = SubmitField('Sign In')

class UploadPhotoForm(FlaskForm):
    friend_name = StringField('Friend\'s Name', validators=[DataRequired()])
    friend_contact = StringField('Friend\'s Contact', validators=[DataRequired()])
    message = StringField('Message', validators=[])
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'JPG and PNG images only!')
    ])
    times_per = SelectField('Times per', choices=['Once a'])  # TODO: check with designer
    duration = SelectField('duration', choices=['Month'])  # TODO: check with designer
    submit = SubmitField('Submit')  # TODO: check with designer, missing in design
