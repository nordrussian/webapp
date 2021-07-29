import os

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/lecturer_db'  # add :localhost:5432/c
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False  # add
UPLOAD_FOLDER = 'UPLOAD_FOLDER'
SECRET_KEY = 'you-will-never-guess'


#export FLASK_APP=lector && FLASK_ENV=development && fla 