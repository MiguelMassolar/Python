from sys import exit

print("Bem vindo a sua calculadora! Por favor escolha uma das opcções abaixo: ")
escolha = input("1 - SOMA, 2 - SUBTRAÇÃO, 3 - MULTIPLICAÇÃO, 4 - DIVISÃO, 5 - SAIR: ")

if (escolha == "1"):
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    soma = num1 + num2
    print(f'A soma entre {num1} e {num2} é: {soma}')

if (escolha == "2"):
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    sub = num1 - num2
    print(f'A subtração entre {num1} e {num2} é: {sub}')

if (escolha == "3"):
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    multi = num1 * num2
    print(f'O resultado da multiplicação entre {num1} e {num2} é: {multi}')

if (escolha == "4"):
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    divi = num1 / num2
    print(f'O resultado da divisão entre {num1} e {num2} é: {divi}')

if (escolha == "5"):
    print("OK, volte outra hora!")
    exit()
