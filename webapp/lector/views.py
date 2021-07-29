#  from webapp.db import db
from webapp.lector.forms import AddForm
from flask import Blueprint, redirect, render_template, flash
from webapp.db import db
from webapp.lector.models import Lecturer

blueprint = Blueprint('lector', __name__)

@blueprint.route("/", methods=['POST', 'GET']) # add
def home():
    # return 'Hello123545'
    all_lectors = Lecturer.query.all()
    return render_template("index.html", all_lectors=all_lectors)  # add


@blueprint.route('/add-lector')
def add_lector():
     form = AddForm()
     return render_template('add-lector.html', form=form)

@blueprint.route('/add-lector-process', methods=['POST'])
def add_lector_process(): 
    form = AddForm()
    new_lecturer = Lecturer(name=form.name.data, 
                            lastname=form.lastname.data,
                            middlename=form.middlename.data,
                            birthday=form.birthday.data,
                            tel=form.tel.data,
                            email=form.email.data,
                            city=form.city.data,
                            passport_number=form.passport_number.data,
                            passport_who=form.passport_who.data,
                            issued=form.issued.data,
                            adress=form.adress.data,
                            agreement_number=form.agreement_number.data,
                            work=form.work.data,
                            created_at=form.created_at.data,
                            rang=form.rang.data)
    db.session.add(new_lecturer)
    db.session.commit()
    flash ('Лектор добавлен') 
    return render_template('index.html', form=form)

    

# @blueprint.route('/all-lectors')
# def all_lectors():
#     all_lectors = Lecturer.query.order_by(Lecturer.surname).all()
#     return render_template("all-lectors.html", all_lectors=all_lectors, title="Список всех лекторов")

# @blueprint.route('/all-lectors/<int:lecturer_id>') # Cтраничка лектора
# def lector_detail(lecturer_id):
#     lector = Lecturer.query.get(lecturer_id)
#     return render_template("lector.html", title="Страница лектора", lector=lector)
    

# @blueprint.route('/all-lectors/<int:lecturer_id>/delete') #Удаление лектора из базы
# def lector_delete(lecturer_id):
#     lector = Lecturer.query.get_or_404(lecturer_id)
#     try:
#         # db.session.delete(lector)
#         # db.session.commit()
#         return redirect('/')
#     except:
#         return "При удалении произошла ошибка"

# @blueprint.route('/all-lectors/<int:lecturer_id>/update', methods=['POST','GET'])
# def lector_update(lecturer_id):
#     if request.method == "POST":
#         lecturer = Lecturer.query.get(lecturer_id) 
#         lecturer.surname = request.form['surname']
#         lecturer.lastname = request.form['lastname']
#         lecturer.middlename = request.form['middlename']
#         lecturer.birthday = request.form['birthday']
#         lecturer.tel = request.form['tel']
#         lecturer.email = request.form['email']
#         lecturer.city = request.form['city']
#         lecturer.passport_number = request.form['passport_number']
#         lecturer.passport_who = request.form['passport_who']
#         lecturer.issued = request.form['issued']
#         lecturer.adress = request.form['adress']
#         lecturer.agreement_number = request.form['agreement_number']
#         lecturer.work = request.form['work']
#         lecturer.created_at = request.form['created_at']
#    #     lecturer.status = request.form['status']
#         lecturer.rang = request.form['rang']        
#         # db.session.commit() # подтверждение изменений
#         return redirect(f'/all-lectors/{lecturer_id}/success-lector') # проброс на страницу лектора
        
#     else:
#         new_lecturer = Lecturer.query.get(lecturer_id)
#         # считывает из таблицы лекторов все строчки и сортировка по дате добавления
#     return render_template("lector-update.html", lector=new_lecturer, title="Редактирование информации о лекторе")
