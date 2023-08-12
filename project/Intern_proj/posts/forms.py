from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,FileAllowed

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    video_link=StringField('youtoube video')
    image_file = FileField('picture', validators=[DataRequired(),FileAllowed(['jpg', 'png'])])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')    