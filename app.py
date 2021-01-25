import os
from flask import Flask, request, flash, render_template, redirect, url_for
from config import Config 
from forms import UploadForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'index'

def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    form = UploadForm()

    if request.method == 'POST':
        
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect("google.com")
        file = request.files['file']
        
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect("facebook.com")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploader',
                                    filename=filename))

    return render_template('uploader.html', form=form)