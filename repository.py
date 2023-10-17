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

def gerar_id():
    id = len(personagens) + 1
    return id

def criar_personagem(nome, raca, casa, altura, nascimento, imagem):
    personagens[gerar_id()] = {"nome":nome, "raca":raca, "casa":casa, "altura":altura, "nascimento":nascimento, "imagem":imagem}
    
def retornar_personagens():
    return personagens

def retornar_personagem(id:int):
    if id in personagens.keys():
        return personagens[id]
    else:
        return {}
    
def atualizar_personagem(id:int, dados_personagem:dict):
    personagens[id] = dados_personagem
    
def remover_personagem(id:int):
    del personagens[id]

print(retornar_personagens())

criar_personagem("Joel", "Humana", "Casa", 1.65, "13/08/1984", "")

print(retornar_personagem(5))

atualizar_personagem(5, {'nome': 'Samuel', 'raca': 'Humana', 'casa': 'Casa', 'altura': 1.65, 'nascimento': '13/08/1984', 'imagem': ''})

print(retornar_personagem(5))

remover_personagem(5)

print(retornar_personagem(5))