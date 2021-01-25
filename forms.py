from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired

class UploadForm(FlaskForm):
    afile = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')