a = input('Digite algo: ')
print('A tipo primitivo desse valor é: ', type(a))#Vericia o tipo da var
print('Só tem espaços? ', a.isspace())#Verifica se á espaços.
print('É um número? ', a.isnumeric())#Verifica se é numérico.
print('É alfabético? ', a.isalpha())#Verifica se é alfanumérico.
print('É alfanumérico? ', a.isalnum())#Verifica se é um número.
print('Está em maiúscula? ', a.isupper())#Identifica se TUDO está maiúsculo.
print('Está em minúscula? ', a.islower())#Identifica se TUDO está minúsculo.
print('Está capitalizada? ', a.istitle())#Identifica se a 1° está Capitalizada.