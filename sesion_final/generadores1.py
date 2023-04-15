
lista = [1,2,3,4,5,6]

for i in lista:
    print(i)

# generador es un tipo de dato.
# se basa en una palabra reservada yield que es un return peculiar
# el resultado es a demanda
# si no hay salta excepcion StopIteration
# con un generador solo se carga la lista a demanda. No la carga toda solo la que usa.



def generador1():
    yield 1
    yield lista


generador = generador1()
# print(type(generador))   # printa <class 'generator'>


resultado = next(generador)
print((resultado))

 generador es un tipo de dato.

# se basa en una palabra reservada yield que es un return peculiar
# el resultado es a demanda
# si no hay salta excepcion StopIteration
# con un generador solo se carga la lista a demanda. No la carga toda solo la que usa.

def obtener_items():
     for i in lista:
          yield i

for item in obtener_items():
        print(item)

