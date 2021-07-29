import os
from flask import Flask, flash, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy  # add
from flask_migrate import Migrate
from datetime import datetime  # add
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from werkzeug.utils import secure_filename




# from lector import Lecturer

# WTF-Form-validation
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# images for lectors upload


UPLOAD_FOLDER = '/uploads/lector'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/lecturer_db'  # add :localhost:5432/c
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # add
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = SQLAlchemy(app)  # add
migrate = Migrate(app, db)






# @app.route('/lector/<int:id>')
# def lector(surname, id):
#         return 'Страница лектора' + surname + 'id'


# @app.route('/delete/<int:id>') # remove a task
# def delete(id):
#    task = Lecturer.query.get_or_404(id)

#    try:
#        db.session.delete(task)
#        db.session.commit()
#        return redirect('/')
#    except Exception:
#        return "There was a problem deleting data."

# # update task
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#    task = Lecturer.query.get_or_404(id)

#    if request.method == 'POST':
#        task.name = request.form['name']

#        try:
#            db.session.commit()
#            return redirect('/update.html')
#        except:
#            return "There was a problem updating data."

#    else:
#        title = "Update Task"
#        return render_template('update.html', title=title, task=task)

if __name__ == "__main__":
   app.run(debug=True)
