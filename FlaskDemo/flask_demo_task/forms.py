from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_demo_task.models import User

class CreateUser(FlaskForm):
    name = StringField('Name', validators = [DataRequired(), Length(min=2, max=40)])
    email = StringField('Email ID: ', validators = [DataRequired(), Email()])
    company = StringField('Company Name', validators = [DataRequired(), Length(max=40)])
    mobile_no = IntegerField('Mobile Number', validators = [DataRequired()])
    submit = SubmitField('Submit details') 

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')