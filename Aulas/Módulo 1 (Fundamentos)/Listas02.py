lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme')) #imprime a posição do conteúdo especificado.
#print(lista.index(42)) Acontecerá um erro pois 42 não está na lista!
print(lista[2])
print(1 in lista)
print('Rebeca' in lista)
print('Pedro' not in lista)
print(lista[0])
print(lista[4])
#print(lista[5]) Retornará "list index out of range" porque a posição digitada não existe dentro da lista.
print(lista[-1]) #Retornará os valoresda lista no sentido inverso.
print(lista[-5])