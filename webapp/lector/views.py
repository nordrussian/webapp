#  from webapp.db import db
# from lector.forms import AddForm
from flask import Blueprint, redirect, render_template
# from webapp.lector.models import Lecturer

blueprint = Blueprint('lector', __name__)

@blueprint.route("/", methods=['POST', 'GET']) # add
def home():
    return 'Hello123545'
    all_lectors = Lecturer.query.all()
    return render_template("index.html", all_lectors=all_lectors)  # add


# @blueprint.route('/add-lector', methods=['POST','GET'])
# def add_lector():
#     form = AddForm()
#     return render_template('html', form=form)

#     if request.method == "POST":
#         name = request.form['surname']
#         lastname = request.form['lastname']
#         middlename = request.form['middlename']
#         birthday = request.form['birthday']
#         tel = request.form['tel']
#         email = request.form['email']
#         city = request.form['city']
#         passport_number = request.form['passport_number']
#         passport_who = request.form['passport_who']
#         issued = request.form['issued']
#         adress = request.form['adress']
#         agreement_number = request.form['agreement_number']
#         work = request.form['work']
#         created_at = request.form['created_at']
#    #     status = request.form['status']
#         rang = request.form['rang']
#         new_lecturer = Lecturer(name=name, lastname=lastname, 
#         middlename=middlename, birthday=birthday, tel=tel, email=email, 
#         city=city, passport_number=passport_number, passport_who=passport_who, 
#         issued=issued, adress=adress, agreement_number=agreement_number, work=work,
#         created_at=created_at, rang=rang ) # создаем объект в памяти соответствующий БД
#         # db.session.add(new_lecturer) # Вставка алхимии в строчку
#         # db.session.commit() # подтверждение изменений
#         return redirect('/add-success') # проброс на главную
        
#     else:
#         new_lecturer = Lecturer.query.order_by(Lecturer.created_at).all()  # считывает из таблицы лекторов все строчки и сортировка по дате добавления
# #     return render_template("add-lector.html", title="Добавление лектора в базу")

    

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
