import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

CURSOS = [
    {
        "id": 1,
        "nome": "Informatica",
        "descrição": "Aqui você podera aprender sobre diversas areas da informatica",
        "carga_horaria": "3.450 horas",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR6uawwzTshrsICaFbcVoJ106hNgKSbm1K3w&s",
        "descrição_detalhada":"O curso de Informática prepara o aluno para utilizar computadores, softwares e ferramentas tecnológicas de forma eficiente no dia a dia profissional. Os estudantes aprendem desde os fundamentos do sistema operacional até aplicações mais avançadas, como programação básica, manutenção de computadores e uso de ferramentas de produtividade. É ideal para quem deseja se inserir no mercado de trabalho, melhorar suas habilidades digitais ou atuar em áreas que exigem conhecimento tecnológico."

    },
    {
        "id": 2,
        "nome": "Administração",
        "descrição": "Aqui você podera aprender sobre diversos assuntos da area da administração",
        "carga_horaria": "3.200 horas",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRumdwbyXEdO8X7K8OnxS7K8ORWeC9P7L3xfQ&s",
        "descrição_detalhada":"O curso de Administração desenvolve competências para gerenciar empresas, pessoas, recursos e processos com foco em resultados. Nele, o aluno aprende sobre planejamento, organização, liderança, finanças, marketing, atendimento ao cliente e empreendedorismo. É um curso versátil, indicado para quem deseja atuar em diversos setores do mercado ou abrir o próprio negócio, oferecendo uma visão completa do funcionamento de uma organização."
    },
    {
        "id": 3,
        "nome": "Vestuario",
        "descrição": "Aqui você podera aprender sobre diversos modos de custura na area de vestuario",
        "carga_horaria": "3.200 horas",
        "imagem":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjk-uKt4lJUAWgLNL8b7vR5wdnpB1fLxzxag&s",
        "descrição_detalhada": "O curso de Vestuário forma profissionais capacitados para atuar na criação, modelagem e produção de roupas e acessórios. Os alunos aprendem sobre desenho técnico, corte e costura, tendências de moda, reciclagem têxtil, criação de peças e operação de máquinas industriais. É ideal para quem deseja trabalhar com moda, confecção ou design de roupas, desenvolvendo criatividade e habilidades práticas para o setor têxtil."
    }
]


@app.route("/")
def index():
    return render_template("index.html",CURSOS = CURSOS)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/curso/<int:id>")
def curso(id):
    curso_selecionado = None

    for c in CURSOS:
        if c.get("id") == id:
            curso_selecionado = c
            break

    if curso_selecionado:
        return render_template("curso.html", curso=curso_selecionado)
    else:
        return "Curso não encontrado", 404



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)