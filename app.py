import os
import time
import imghdr
from flask import Flask, flash, render_template, redirect, url_for, abort, send_from_directory
from config import Config 
from forms import UploadForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        file_ext = os.path.splitext(filename)[1].lower()
        if filename != '':
            if file_ext != validate_image(f.stream):
                return render_template('uploader.html', form=form, invalid='Invalid image format!')
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], time.strftime('%Y%m%dT%H%M%S', time.gmtime()) + file_ext))
        return redirect(url_for('index'))
    return render_template('uploader.html', form=form)

@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)