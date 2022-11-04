from flask_wtf import FlaskForm
from wtforms import EmailField, TextAreaField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    text = TextAreaField('text', validators=[DataRequired()])
