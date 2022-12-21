a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))

print(len(a))
print(a.__len__())

print('1' in a)
a.__contains__('1')