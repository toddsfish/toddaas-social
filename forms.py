from flask_wtf import FlaskForm
from config import Config
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    file = FileField(validators=[FileRequired(), FileAllowed(Config.ALLOWED_EXTENSIONS, 'Must be .jpg or .jpeg files')])
    submit = SubmitField('Upload')