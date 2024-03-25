contato = {"nome": "Gabriel", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovana")  # "Gabriel"
print(contato)  # {'nome': 'Gabriel', 'telefone': '3333-2221'}

contato.setdefault("idade", 22)  # 22
print(contato)  # {'nome': 'Gabriel', 'telefone': '3333-2221', 'idade': 28}