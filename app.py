import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

CURSOS = [
    {
        "id": 1,
        "nome": "Informatica",
        "descrição": "Aqui você podera aprender sobre diversas areas da informatica",
        "carga_horaria": "3.450 horas",
        "imagem": ""

    },
    {
        "id": 2,
        "nome": "Administração",
        "descrição": "Aqui você podera aprender sobre diversos assuntos da area da administração",
        "carga_horaria": "3.200 horas",
        "imagem": ""
    },
    {
        "id": 3,
        "nome": "Vestuario",
        "descrição": "Aqui você podera aprender sobre diversos modos de custura na area de vestuario",
        "carga_horaria": "3.200 horas",
        "imagem":""
    }
]


@app.route("/")
def index():
    return render_template("index.html",curso = CURSOS)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)