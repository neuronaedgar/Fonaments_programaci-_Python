
'''
a,b,c,d = (1,2,3,4)  # unboxing

def procesar(a,b,c):
    return a + b + c


procesar(1,3,6)
'''

def procesar(*numeros):  # numero indefinado de parámetros
    return sum(numeros)

print(procesar(1,3,4,6,7,8))


tupla = (2,5,7)
#print(procesar(tupla))  # Error unsupported operand type(s) for +: 'int' and 'tuple'
print(procesar(*tupla))

lista = [2,4,6]
print(procesar(*lista))









