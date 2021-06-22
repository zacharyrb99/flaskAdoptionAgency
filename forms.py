from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Pet Species', choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')])
    photo_url = StringField('Pet Photo URL', validators=[Optional(), URL(message='Must be a URL')])
    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Pet Notes')
    available = SelectField('Is the Pet Available?', choices=[(True, True), (False, False)])