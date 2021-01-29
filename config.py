import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # Don’t read more than this many bytes from incoming request data.
    MAX_CONTENT_LENGTH = 1024 * 1024 * 10
    UPLOAD_FOLDER = './uploads'
    ALLOWED_EXTENSIONS = ['txt','jpg','jpeg']