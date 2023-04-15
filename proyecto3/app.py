
# lambdas 

sumar = lambda a, b : a + b

def calcular(x: int, y: int, f) -> int:
    return f(x, y)

resultado = calcular(9, 5, sumar)
print(f"El resulado es {resultado}")


resultado = calcular(9,5, lambda x,y: x -y)
print(f"El resulado es {resultado}")

'''

resultado = calcular(9,5, lambda x: x - 2)   # Error pq debemos pasar 2 parámetros TypeError: <lambda>() takes 1 positional argument but 2 were given
print(f"El resulado es {resultado}")

'''

def multiplicar(a:int, b:int) -> int:
    return a*b

resultado = calcular(9,5, multiplicar)
print(f"El resulado es {resultado}")


# HOF -> High Order Function son funciones que devuelven 

'''
def procesar(a:float, b:float) -> any:
    f = lambda x, y : a + b
    return f

my_funcion = procesar(10.5,1.5)
resultado =my_funcion()
print(f"El resulado es {resultado}")

'''

# MAP -> transformar todos los elementos de una funcion en otra cosa. y los devuelve en otra coleccion.

items = [1,2,3,4,5,6]
multiplicar_3 = lambda x : x * 3

items_multiplicados_por_3 = map(multiplicar_3, items) # me devuelve un map tengo que hacer un casting
print(items_multiplicados_por_3)


items_multiplicados_por_3 = list(map(multiplicar_3, items))
print(items_multiplicados_por_3)

items_2 = range(1,256)
items_multiplicados_por_3 = list(map(multiplicar_3, items_2))
print(items_multiplicados_por_3[:20])

# Filter -> filtrar unos elementos que cumplan una o unas determinadas condiciones.

import random

items_3 = list(range(1,256))
#print(random.shuffle(items_3))

resultado_mayor_23 = list(filter(lambda x : x > 53, items_3))
print(resultado_mayor_23)

