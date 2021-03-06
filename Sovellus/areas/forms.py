from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AreaForm(FlaskForm):
    name = StringField("Name of the area", [validators.Length(min=1)])
 
    class Meta:
        csrf = False