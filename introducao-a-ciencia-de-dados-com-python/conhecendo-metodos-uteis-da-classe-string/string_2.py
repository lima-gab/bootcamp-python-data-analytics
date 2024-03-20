nome = 'Gabriel'
idade = 22
profissao = 'Programador'
linguagem = 'Python'
saldo = 45.435

dados = {'nome': 'Gabriel',
         'idade': 22
         }

print('Nome: %s Idade %d' % (nome, idade))

print('Nome: {1} Idade {0}'.format(idade, nome))

print('Nome: {1} Idade {0} Nome: {1} {1}'.format(idade, nome))

print('Nome: {name} Idade {age}'.format(age=idade, name=nome))

print('Nome: {nome} Idade: {idade}'.format(**dados))

print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}')

print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')