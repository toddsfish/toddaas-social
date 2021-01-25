import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}