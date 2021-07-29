from events.db import db


class Events(db.Model): # отсюда  https://pythobyte.com/using-sqlalchemy-with-flask-and-postgresql-056e4a45/
    
    event_id = db.Column(db.Integer, primary_key=False) # id мероприятия
    event_name = db.Column(db.String(80), nullable=False) # Название мероприятия
    event_date = db.Column(db.DateTime, nullable=False) # Дата мероприятия
    event_lector = db.Column(db.String(80), nullable=False) # Лектор мероприятия
   
    event_lection_name = db.Column(db.String(80), nullable=False) # Название лекции
    event_lection_place = db.Column(db.Text, nullable=False) # Место проведения
    event_lection_drug = db.Column(db.String, nullable=False) # Препарат 
    event_lection_starttime = db.Column(db.DateTime, nullable=False) # время начала мероприятия
    event_lection_stoptime = db.Column(db.DateTime, nullable=False) # время окончания мероприятия
    event_lection_duration = db.Column(db.Integer, nullable=False) #Длительность лекции
    event_lection_cost = db.Column(db.String, nullable=False) # Cost - центр 
    event_lection_transport = db.Column(db.Boolean, nullable=True) # Транспортные расходы 
    event_lection_living = db.Column(db.Boolean, nullable=True) # Расходы на проживание

    def __repr__(self):
        return f'Lecturer : {self.surname} {self.lastname} {self.middlename}, {self.email}, {self.tel}, {self.work}'