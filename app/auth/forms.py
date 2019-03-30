from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError

from ..models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[Required(), Length(1, 64), Email()])
    username = StringField("Username", validators=[
        Required(),
        Length(1, 64),
        Regexp(
            regex='^[A-Za-z][A-Za-z0-9_.]*$',
            flags=0,
            message="Username must have only letters, numbers, dots or underscores"
        )
    ])
    password = PasswordField("Password", validators=[
        Required(),
        EqualTo("password_confirmation", message="Password must match")
    ])
    password_confirmation = PasswordField("Confirm password", validators=[Required()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use")
