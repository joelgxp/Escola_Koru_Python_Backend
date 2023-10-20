from flask import Flask, redirect, render_template, request, url_for
import repository

app = Flask(__name__)

@app.route("/")
def home():
    dicionario = repository.retornar_personagens()
    return render_template("index.html", dados=dicionario)

@app.route("/personagem/<int:id>", methods=["GET", "POST"])
def editar_personagem(id):

    if request.method == "POST":
        
        if "excluir" in request.form:
            repository.remover_personagem(id)
            return redirect(url_for("home"))
        elif "salvar" in request.form:
            personagem = {}
            personagem["nome"] = request.form["nome"]
            personagem["raca"] = request.form["raca"]
            personagem["casa"] = request.form["casa"]
            personagem["altura"] = request.form["altura"]
            personagem["nascimento"] = request.form["nascimento"]
            personagem["imagem"] = request.form["imagem"]
        
            if id in repository.retornar_personagens().keys():
                repository.atualizar_personagem(id, personagem)
                return redirect(url_for("home"))
    else:        
        personagem = repository.retornar_personagem(id)
        personagem["id"] = id
        return render_template("cadastro.html", **personagem)
    
@app.route("/personagem", methods=["GET", "POST"])
def criar_personagens():
    if request.method == "POST":
        personagem = {}
        personagem["nome"] = request.form["nome"]
        personagem["raca"] = request.form["raca"]
        personagem["casa"] = request.form["casa"]
        personagem["altura"] = request.form["altura"]
        personagem["nascimento"] = request.form["nascimento"]
        personagem["imagem"] = request.form["imagem"]
        repository.criar_personagem(**personagem)
        return redirect(url_for("home"))
    else:
        return render_template("cadastro.html", id=repository.gerar_id())

app.run(debug=True)