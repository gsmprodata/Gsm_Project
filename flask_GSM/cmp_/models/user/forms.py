from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Email,Length

class login_form (FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=2,max=10)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('Login')
    
