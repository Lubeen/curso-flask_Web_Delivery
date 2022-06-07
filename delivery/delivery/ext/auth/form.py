import wtforms as wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class UserForm(FlaskForm):
    email = wtf.StringField("Email", [wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField('Senha', [wtf.validators.DataRequired(), wtf.validators.Length(min=6)])
    confirm_password = wtf.PasswordField('Confirmar senha', [wtf.validators.DataRequired(), wtf.validators.EqualTo('password')])
    foto = FileField('Foto')