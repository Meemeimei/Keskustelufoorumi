from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import TextArea

class GroupForm(FlaskForm):
    name = StringField("GroupName", [validators.Length(min=5)])
 
    class Meta:
        csrf = False