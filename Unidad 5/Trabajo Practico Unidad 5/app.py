from flask import Flask, render_template, session, request, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Trabajador, Registro

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/acceso_trabajador')
def acceso_trabajador():
    return render_template('acceso_trabajador.html')

@app.route('/registro_entrada', methods=['GET', 'POST'])
def registro_entrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_final = request.form['dni']
        dependencia = request.form['dependencia']

        #verifica si el trabajador existe y si el DNI termina con el valor ingresado
        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador or not trabajador.dni.endswith(dni_final):
            flash('Datos incorrectos', 'error')
            return redirect('/registro_entrada')

        #verifica si ya existe un registro de entrada para el trabajador en el día actual
        hoy = datetime.today().date()
        registro_existente = Registro.query.filter_by(idtrabajador=trabajador.id, fecha=hoy).first()
        if registro_existente:
            flash('Ya registraste entrada hoy.', 'warning')
            return redirect('/registro_entrada')

        # Si todo es correcto, crea un nuevo registro de entrada
        nuevo_registro = Registro(fecha=hoy, horaentrada=datetime.now().time().replace(microsecond=0), dependencia=dependencia, idtrabajador=trabajador.id)
        db.session.add(nuevo_registro)
        db.session.commit()
        flash('Entrada registrada correctamente.', 'success')
        return redirect('/registro_entrada')
    # Si es un GET, muestra el formulario de registro de entrada
    return render_template('registro_entrada.html')

@app.route('/registro_salida', methods=['GET', 'POST'])
def registro_salida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_final = request.form['dni']

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador or not trabajador.dni.endswith(dni_final):
            flash('Datos incorrectos', 'error')
            return redirect('/registro_salida')

        hoy = datetime.today().date()
        registro = Registro.query.filter_by(idtrabajador=trabajador.id, fecha=hoy).first()

        if not registro:
            flash('No se encontró entrada registrada para hoy.', 'warning')
            return redirect('/registro_salida')

        if registro.horasalida:
            flash('Ya registraste tu salida hoy.', 'info')
            return redirect('/registro_salida')

        return render_template('registro_salida.html', registro=registro)
    # Si es un GET, muestra el formulario de registro de salida
    return render_template('registro_salida.html')

@app.route('/confirmar_salida', methods=['POST'])
def confirmar_salida():
    registro_id = request.form['registro_id']
    registro = Registro.query.get(registro_id)

    if not registro or registro.horasalida:
        flash('Error al confirmar la salida.', 'error')
        return redirect('/salida')

    registro.horasalida = datetime.now().time().replace(microsecond=0)
    db.session.commit()
    flash('Salida registrada correctamente.', 'success')
    return redirect('/registro_salida')

@app.route('/consulta_registros', methods=['GET', 'POST'])
def consulta_registros():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_final = request.form['dni']
        inicio_periodo = request.form['inicio_periodo']
        fin_periodo = request.form['fin_periodo']

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador or not trabajador.dni.endswith(dni_final):
            flash('Datos incorrectos', 'error')
            return redirect('/consulta_registros')

        try:
            inicio = datetime.strptime(inicio_periodo, '%Y-%m-%d').date()
            fin = datetime.strptime(fin_periodo, '%Y-%m-%d').date()
        except ValueError:
            flash('Formato de fecha inválido.', 'error')
            return redirect('/consulta_registros')

        registros = Registro.query.filter(Registro.idtrabajador == trabajador.id, Registro.fecha.between(inicio, fin)).order_by(Registro.fecha).all()
        return render_template('consulta_registros.html', registros=registros, trabajador=trabajador)
    # Si es un GET, muestra el formulario de consulta
    return render_template('consulta_formulario.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)