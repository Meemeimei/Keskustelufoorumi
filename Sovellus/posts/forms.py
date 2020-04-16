from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PostForm(FlaskForm):
    name = StringField("Title", [validators.Length(min=5)])
    text = StringField("", [validators.Length(min=5)])
 
    class Meta:
        csrf = False