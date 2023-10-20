from datetime import datetime
import sqlite3

personagens = {
    1: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": ""
    },
    2: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": ""
    },
    3: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": ""
    },
    4: {
        "nome": "Harry Potter",
        "raca": "Humano",
        "casa": "Grifinória",
        "altura": 1.80,
        "nascimento": "31/07/1980",
        "imagem": ""
    }
}

def tratar_iso_para_dmy(data:str):
    if "-" in data:
        data = datetime.strptime(data, "%Y-%m-%d")
        return data.strftime("%d/%m/%Y")
    else:
        return data
    
def tratar_dmy_para_iso(data:str):
    if "/" in data:
        data = datetime.strptime(data, "%d/%m/%Y")
        return data.strftime("%Y-%m-%d")
    else:
        return data

def gerar_id():
    conn = sqlite3.connect("jogo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens")
    next_id = cursor.fetchone()[0]
    return next_id + 1

def criar_personagem(nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect("jogo.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) VALUES(?,?,?,?,?,?)"
        cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))
        personagem_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return personagem_id    
    except Exception as e:
        print(e)
        return 0
    
def retornar_personagens():
    for id, personagem in personagens.items():
        personagem["nascimento"] = tratar_iso_para_dmy(personagem["nascimento"])
    return personagens

def retornar_personagem(id:int):
    if id in personagens.keys():
        personagens[id]['nascimento'] = tratar_dmy_para_iso(personagens[id]['nascimento'])
        return personagens[id]
    else:
        return {}
    
def atualizar_personagem(id:int, nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect("jogo.db")
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome_personagem = ?, raca_personagem = ?, casa_personagem = ?, altura_personagem = ?, nascimento_personagem = ?, imagem_personagem = ? WHERE id = ?"
        personagens[id]['nome'] = nome
        personagens[id]['raca'] = raca
        personagens[id]['casa'] = casa
        personagens[id]['altura'] = altura
        personagens[id]['nascimento'] = nascimento
        personagens[id]['imagem'] = imagem
        return True
    
    
def remover_personagem(id:int):
    del personagens[id]
