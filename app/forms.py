from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
 
class InputTextForm(FlaskForm):
  inputText = TextAreaField(validators=[DataRequired()])
