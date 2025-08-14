from flask_wtf import FlaskForm
from wtforms import StringField , DecimalField, BooleanField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    name = StringField('Nom de la tache', validators = [DataRequired(), Length(min=2, max=50)])
    deadline = StringField('Date limite', validators = [DataRequired(), Length(min=5, max=10)])
    done = BooleanField(' ', default=False)