contatos = {
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "3443-2121"},
    "bianca@gmail.com": {"nome": "Bianca", "telefone": "3344-9871"},
    "rayane@gmail.com": {"nome": "Rayane", "telefone": "3333-7766"},
}

del contatos['gabriel@gmail.com']['telefone']
del contatos['bianca@gmail.com']

contatos # {'gabriel@gmail.com': {'nome': 'Gabriel'}, 'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3443-2121'}, 'rayane@gmail.com': {'nome': 'Rayane', 'telefone': '3333-7766'}}