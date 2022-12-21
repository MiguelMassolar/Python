pessoa = {'nome':'Prof(a).Ana', 'idade': 38, 'cursos': ['Inglês', 'Portugês']}
print(type(pessoa))
print(len(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))