from flask import make_response

JSON_MIME_TYPE = 'application/json'


def obtenerAlumno(alumno, alumno_DNI):
    for alumn in alumno:
        if alumn['DNI'] == alumno_DNI:
            return alumn


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
