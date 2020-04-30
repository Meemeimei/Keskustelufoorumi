from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AnswerForm(FlaskForm):
    content = StringField("Reply", [validators.Length(min=1)])
 
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    content = StringField("Reply", [validators.Length(min=1)])
 
    class Meta:
        csrf = False