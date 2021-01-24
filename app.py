from flask import Flask
from config import Config
from flask import render_template
from forms import UploadForm


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'index'

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    form = UploadForm()
    return render_template('uploader.html', form=form)