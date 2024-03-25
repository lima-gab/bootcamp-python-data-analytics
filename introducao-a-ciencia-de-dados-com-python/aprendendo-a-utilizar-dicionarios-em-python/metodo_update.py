contatos = {"gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"}}

contatos.update({"gabriel@gmail.com": {"nome": "Gab"}})
print(contatos)  # {'gabriel@gmail.com': {'nome': 'Gab'}}

contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "3322-8181"}})
# {'gabriel@gmail.com': {'nome': 'Gab'}, 'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3322-8181'}}
print(contatos)