from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, DateField, IntegerField
from wtforms.validators import Length, EqualTo, DataRequired, Email, ValidationError
from ...database.db import get_db

class FormPreres(FlaskForm):

    usuario = StringField(validators=[Length(min=2, max=100),DataRequired()])
    email = EmailField(validators=[Email(),DataRequired()])
    checkin = DateField(format="%d.%m.%Y",validators=[DataRequired()])
    checkout = DateField(format="%d.%m.%Y",validators=[DataRequired()])
    hspadulto = IntegerField(default=1,validators=[DataRequired()])
    hspcrianca = IntegerField(default=0,validators=[DataRequired()])
    submit = SubmitField(label="Enviar")
