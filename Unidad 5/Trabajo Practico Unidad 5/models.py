from __main__ import app
from flask_sqlalchemy import SQLAlchemy    

db= SQLAlchemy(app)

class Trabajador(db.Model):
    __tablename__ = 'trabajador'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    dni = db.Column(db.Integer, nullable = False, unique = True)
    correo = db.Column(db.String(80), nullable = False, unique = True)
    legajo = db.Column(db.String(10), nullable = False, unique = True)
    horas = db.Column(db.Integer, nullable = False)
    funcion = db.Column(db.String(2), nullable = False)
    registro = db.relationship('Registro', backref='trabajador')

class Registro(db.Model):
    __tablename__ = 'registrohorario'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable = False)
    horaentrada = db.Column(db.Time, nullable = False)
    horasalida = db.Column(db.Time, nullable = False)
    dependencia = db.Column(db.String(3), nullable = False)
    idtrabajador = db.Column(db.Integer, db.ForeignKey('trabajador.id'), nullable = False)