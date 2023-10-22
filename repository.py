from datetime import datetime
import sqlite3

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
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='personagens'")
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
    
def atualizar_personagem(id:int, nome, raca, casa, altura, nascimento, imagem):
    try:
        conn = sqlite3.connect("jogo.db")
        cursor = conn.cursor()
        sql_update = "UPDATE personagens SET nome_personagem = ?, raca_personagem = ?, casa_personagem = ?, altura_personagem = ?, nascimento_personagem = ?, imagem_personagem = ? WHERE id = ?"
        cursor.execute(sql_update, (nome, raca, casa, altura, nascimento, imagem, id))       
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False
    
    
def remover_personagem(id:int):
    try:
        conn = sqlite3.connect("jogo.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_delete, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def retornar_personagens():
    try:
        conn = sqlite3.connect("jogo.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM personagens"
        cursor.execute(sql_select)
        personagens = cursor.fetchall()
        conn.close()
        return personagens
    except:
        return False

def retornar_personagem(id:int):
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", "", ""
        conn = sqlite3.connect("jogo.db")
        cursor = conn.cursor()

        sql_select = "SELECT * FROM personagens WHERE id_personagem = ?"
        cursor.execute(sql_select, (id,))
        id, nome, raca, casa, nascimento, altura, imagem = cursor.fetchone()
        conn.close()
        return id, nome, raca, casa, nascimento, altura, imagem
    except:
        return False
        