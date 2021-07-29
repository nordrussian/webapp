from webapp.db import db


class Lecturer(db.Model): # отсюда  https://pythobyte.com/using-sqlalchemy-with-flask-and-postgresql-056e4a45/
    lecturer_id = db.Column(db.Integer, primary_key=True) # id лектора
    name = db.Column(db.String(80), nullable=False) # Имя
    lastname = db.Column(db.String(80), nullable=False) # Фамилия
    middlename = db.Column(db.String(80), nullable=False) # Отчество
    birthday = db.Column(db.DateTime, nullable=True) # Дата рождения
    tel = db.Column(db.Text, nullable=False) # телефон
    email = db.Column(db.String, nullable=False) # электронная почта
    city = db.Column(db.String(80), nullable=False) # город проживания
    passport_number = db.Column(db.Integer, nullable=True) # Серия и номер паспорта
    passport_who = db.Column(db.Text, nullable=False) # когда и кем выдан
    issued = db.Column(db.DateTime, nullable=True) # Дата выдачи
    adress = db.Column(db.String, nullable=False) # Адрес проживания
    work = db.Column(db.String, nullable=False) # Место работы и адрес
    agreement_number = db.Column(db.String(80), nullable=False) # Номер договора
    created_at = db.Column(db.DateTime, nullable=True) # Дата создания договора
    # status = db.Column(db.Boolean, nullable=True, default=True) # Статус лектора
    rang = db.Column(db.String(32), nullable=False) # ранг КОЛа


    # def __repr__(self):
    #     return f'Lecturer : {self.surname} {self.lastname} {self.middlename}, {self.email}, {self.tel}, {self.work}'