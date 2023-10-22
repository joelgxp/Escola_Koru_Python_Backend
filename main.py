from flask import Flask, redirect, render_template, request, url_for
import repository

app = Flask(__name__)

@app.route("/")
def home():
    lista_personagens = repository.retornar_personagens()
    return render_template("index.html", dados=lista_personagens)

@app.route("/personagem/<int:id>", methods=["GET", "POST"])
def editar_personagem(id):

    if request.method == "POST":
        
        if "excluir" in request.form:
            repository.remover_personagem(id)
            return redirect(url_for("home"))
        elif "salvar" in request.form:
            id = request.form["id"]
            nome = request.form["nome"]
            raca = request.form["raca"]
            casa = request.form["casa"]
            altura = request.form["altura"]
            nascimento = request.form["nascimento"]
            imagem = request.form["imagem"]
        
            dados_retornados = repository.retornar_personagem(id)
            if dados_retornados:
                repository.atualizar_personagem(id=id, nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)
            else:
                repository.criar_personagem(nome=nome, raca=raca, casa=casa, altura=altura, nascimento=nascimento, imagem=imagem)

                return redirect(url_for("home"))
    else:        
        id, nome, raca, casa, nascimento, altura, imagem = repository.retornar_personagem(id)

        return render_template("cadastro.html", id = id, nome = nome, raca = raca, casa = casa, nascimento = nascimento, altura = altura, imagem = imagem)
    
app.run(debug=True)