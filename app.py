import os
from flask import Flask, flash, render_template, redirect, url_for
from config import Config 
from forms import UploadForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'index'

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    return render_template('uploader.html', form=form)