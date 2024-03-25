contatos = {"gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('gabriel@gmail.com', {'nome': 'Gabriel', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError