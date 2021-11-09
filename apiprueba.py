import flask 
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

personajes = [
    {"nombre": "bryan",
    "edad": 25
    },
    {"nombre": "gerson",
    "edad": 24
    },
    {"nombre": "abraham",
    "edad": 22
    },
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Personajes</h1>
<p>Bryan, Gerson, Abraham</p>'''


@app.route('/personajes', methods=['GET'])
def api_all():
    return jsonify(personajes)


@app.route('/personaje/<string:nombre>', methods=['GET'])
def api_nombre(nombre):
 
    
    personajesF = [personaje for personaje in personajes if personaje['nombre'] == nombre]
    return jsonify(personajesF[0])

    
app.run(host='localhost',debug=False, port=3010)


# print(personajes)