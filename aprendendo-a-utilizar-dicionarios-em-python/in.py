contatos = {
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "3443-2121"},
    "bianca@gmail.com": {"nome": "Bianca", "telefone": "3344-9871"},
    "rayane@gmail.com": {"nome": "Rayane", "telefone": "3333-7766"},
}

resultado = 'gabriel@gmail.com' in contatos # True
print(resultado)

resultado = 'rafael@gmail.com' in contatos # False
print(resultado)

resultado = 'idade' in contatos['gabriel@gmail.com'] # False
print(resultado)

resultado = 'telefone' in contatos['giovana@gmail.com'] # True
print(resultado)