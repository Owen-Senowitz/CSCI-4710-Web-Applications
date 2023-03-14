from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ClassmateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    no_shadow = BooleanField('No Shadow')
    pale_complexion = BooleanField('Pale Complexion')
    no_garlic = BooleanField('No Garlic')
    submit = SubmitField('Add Classmate')

class DataProcessingForm(FlaskForm):
    data_processing_method = SelectField('Data Processing Method', choices=[('threshold', 'Threshold Based'), ('random', 'Random Guess')])
    submit = SubmitField('Update Pie Chart')
