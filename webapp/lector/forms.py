from typing import DefaultDict
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField, DataField
from wtforms.validators import DataRequired, Email

class AddForm(FlaskForm):
    name = StringField ('Имя', [DataRequired()])
    lastname = StringField ('Фамилия', [DataRequired()])
    middlename = StringField ('Отчество', [DataRequired()])
    birthday = request.form['birthday']
    tel = StringField ('Телефон', [DataRequired()])
    email = StringField ('E-mail', [DataRequired(), Email()])
    city = StringField ('Город', [DataRequired()])
    passport_number = IntegerField ('Серия и номер паспорта', [DataRequired()])
    passport_who = StringField ('Кем выдан паспорт', [DataRequired()])
    issued = DataField ('Когда выдан паспорт', [DataRequired()])
    adress = StringField ('Адрес проживания', [DataRequired()])
    agreement_number = StringField ('Номер договора', [DataRequired()])
    work = StringField ('Место и адрес работы', [DataRequired()])
    created_at = DataField ('Дата создания договора', [DataRequired()])
    status = RadioField ('Активность лектора', [DataRequired()])
    rang = StringField ('Ранг лектора', [DataRequired()])
# new_lecturer = Lecturer(surname=surname, lastname=lastname, 
# middlename=middlename, birthday=birthday, tel=tel, email=email, 
# city=city, passport_number=passport_number, passport_who=passport_who, 
# issued=issued, adress=adress, agreement_number=agreement_number, work=work,
# created_at=created_at, rang=rang ) # создаем объект в памяти соответствующий БД