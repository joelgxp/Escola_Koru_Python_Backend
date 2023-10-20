import sqlite3

conexao = sqlite3.connect("jogo.db")

nome = "Joel Souza"
raca = "Humano"
casa = "Grifinoria"
altura = 1.80
nascimento = "31/07/1980"
imagem = ""

cursor = conexao.cursor()
sql_insert = "INSERT INTO personagens (nome_personagem, raca_personagem, casa_personagem, altura_personagem, nascimento_personagem, imagem_personagem) VALUES(?,?,?,?,?,?)"
cursor.execute(sql_insert, (nome, raca, casa, altura, nascimento, imagem))

personagem_id = cursor.lastrowid
conexao.commit()