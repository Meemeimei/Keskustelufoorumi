from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=3)])
  
    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    oldPassword = PasswordField("Old password", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=2)])
  
    class Meta:
        csrf = False