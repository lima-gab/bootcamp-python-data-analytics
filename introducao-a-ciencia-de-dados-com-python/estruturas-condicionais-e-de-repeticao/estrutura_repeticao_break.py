while True:
    numero = int(input('Informe um número: '))

    if numero == 10:
        break
    
    print(numero)


for numero in range(100):
    if numero == 12:
        break # cortar execução ao atingir o número 12

    print(numero)

for numero in range(100):
    if numero == 15:
        continue # pular o número 15