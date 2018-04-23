import json
from flask import Flask, Response, abort
from utils import JSON_MIME_TYPE, buscarAlumno

app = Flask(__name__)

alumno = [{
    'DNI': 66666666,
    'Nombre': 'Thomas Iarussi',
    'Materias': ["Saclier", "DiLorenzo"]
},
{
    'DNI': 32457334,
    'Nombre': 'Juan Pedro',
    'Materias': ["Educacion Fisica"]
},
]

@app.route('/alumno')
def listaAlumnos():
    response = Response(
        json.dumps(alumno), status=200, mimetype=JSON_MIME_TYPE)
    return response

@app.route('/alumno/<int:alumno_DNI>')
def detalleAlumno(alumno_DNI):
    alumn = buscarAlumno(alumno, alumno_DNI)
    if alumn is None:
        abort(404)
    content = json.dumps(alumn)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}

@app.route('/alumno/<int:alumno_DNI>/materias')
def materiaAlumno(alumno_DNI):
    alumn = buscarAlumno(alumno, alumno_DNI)
    if alumn is None:
        abort(404)

    data_string = json.dumps(alumn)
    decoded = json.loads(data_string)
    data_string = json.dumps(decoded["Materias"])

    return data_string, 200, {'Content-Type': JSON_MIME_TYPE}


@app.errorhandler(404)
def not_found(e):
    return 'No anda', 404
