from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired,InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    

class ContactForm(FlaskForm):
    fname=StringField('First Name',validators=[DataRequired()])
    lname=StringField('Last Name',validators=[DataRequired()])
    gender = SelectField(label='Gender', choices=[("Male", "Male"), ("Female", "Female")])
    email=StringField('Email',validators=[DataRequired()])
    location=StringField('Location',validators=[DataRequired()])
    biography=TextAreaField('Biography')
    upload = FileField('Profile Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])