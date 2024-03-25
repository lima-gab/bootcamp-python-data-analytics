contatos = {
    'gabriel@gmail.com': {'nome': 'Gabriel', 'telefone': '3333-2221'},
    'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3443-2121'},
    'bianca@gmail.com': {'nome': 'Bianca', 'telefone': '3344-9871'},
    'rayane@gmail.com': {'nome': 'Rayane', 'telefone': '3333-7766'}
    }

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)