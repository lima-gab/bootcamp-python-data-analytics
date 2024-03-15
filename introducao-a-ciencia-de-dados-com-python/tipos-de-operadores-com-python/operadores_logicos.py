# AND = para ser True tudo ter que ser True
# OR = para ser True apenas um tem que ser True

print(True and True) 
print(True and False) 
print(False and False) 
print(True or True) 
print(True or False) 
print(False or False) 

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(expressao_3)