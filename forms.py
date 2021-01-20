from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField
from wtforms.widgets import TextArea


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CreateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"autofocus": True, "autocomplete": 'off'})
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")


class LogInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={"autofocus": True, "autocomplete": 'off'})
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class CommentForm(FlaskForm):
    comment = StringField("", widget=TextArea(), validators=[DataRequired()], render_kw={"placeholder": "Your comment"})
    submit = SubmitField("Add comment")


class EmailContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired()])
    message = StringField("Message", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField("Send")
