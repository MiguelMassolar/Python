from string import Template

nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome, idade)) #Método antigo!
print('Nome: {0} Idade: {1}'.format(nome, idade))#Método Python < 3.6!
print(f'Nome: {nome} Idade: {idade}')#Método mais recente (Python >= 3.6)!

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))