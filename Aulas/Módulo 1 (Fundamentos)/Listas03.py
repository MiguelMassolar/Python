#Lembrando que a lista começa sempre em 0!
lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3]) #Imprime o item 1 da lista, mas não o terceiro.
print(lista[1:])
print(lista[:-1])
print(lista[:]) #Mesmo que acessar a lista normalmente pelo print!
del lista[2] #Deleta um item da lista.
print(lista)
del lista[1:]
print(lista)