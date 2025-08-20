from flask_wtf import FlaskForm
from wtforms import StringField , DecimalField, BooleanField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, EqualTo

class TaskForm(FlaskForm):
    name = StringField('Nom de la tache', validators = [DataRequired(), Length(min=2, max=50)])
    deadline = DateField('Date limite', validators = [DataRequired()])
    done = BooleanField(' ', default=False)
class registerForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired(), Length(min=2, max=50)])
    prenoms = StringField('Prénoms', validators=[DataRequired(), Length(min=2, max=50)])
    sexe = SelectField('Sexe', choices=['Masculin','Féminin'], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=100)])
    mdp= PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6, max=100)])
    mdp_confirmed = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('mdp', message='Les mots de passe doivent correspondre')])
    submit = SubmitField('S\'inscrire')

class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=100)])
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')
class update(FlaskForm):
    name = StringField('Nom de la tache', validators=[DataRequired(), Length(min=2, max=50)])
    deadline = DateField('Date limite', validators=[DataRequired()])
    done = BooleanField(' ', default=False)
    submit = SubmitField('Modifier la tâche')