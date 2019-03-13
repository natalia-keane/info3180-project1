from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    fname=StringField('First Name',validators=[DataRequired()])
    lname=StringField('Last Name',validators=[DataRequired()])
    gender=SelectField('Gender',choices=[('Male', 'Male'), ('Female', 'Female')])
    email=StringField('Email',validators=[DataRequired()])
    location=StringField('Location',validators=[DataRequired()])
    biography=TextAreaField('Biography', validators=[DataRequired()])