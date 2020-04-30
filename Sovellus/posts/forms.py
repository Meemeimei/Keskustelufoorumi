from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PostForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=1)])
    text = StringField("", [validators.Length(min=1)])
 
    class Meta:
        csrf = False