lista = [1, 'Python', [40, 30, 20]]

lista_2 = lista.copy()

print(lista) # [1, 'Python', [40, 30, 20]]

print(id(lista_2), id(lista))

lista_2[0] = 2

print(lista_2) # [2, 'Python', [40, 30, 20]]
print(lista) # [1, 'Python', [40, 30, 20]]