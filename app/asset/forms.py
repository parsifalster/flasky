from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField,TextAreaField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class AssetForm(FlaskForm):
    name = StringField('name',validators=[Required(),Length(5,20)])
    cart = RadioField('cart',choices=[(1,'TypeOne'),(2,'TypeTwo'),(3,'TypeThree')],default=1)
    desc = TextAreaField('desc')
    submit = SubmitField('new')
    cancel = SubmitField('cancel')


