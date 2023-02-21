# Estructura datos - Diccionarios


palabras = dict() # diccionario vacio y no permite duplicados, por lo que actualiza la clave ya existente.

# palabras = {clave:valor}

palabras = {'Saludos':'Accion de saludar',
            'andar':'accion de desplazarse a pie',
            'programar':'codificar en lenguaje de programacion'}

print(palabras['andar'])

if 'nadar' not in palabras:
        palabras['nadar'] = 'accion de nadar'

if 'nadar' in palabras:
    print(palabras['nadar'])
else:
    print(palabras['andar'])

del palabras['nadar']

print(palabras.get('nadar'))
print(palabras.get('programar2')) # el .get no peta si no existe. 
 
# print(palabras['nadar']) # Da un error KeyError: 'nadar' porque lo he borrado del diccionario

# recorreido
for par in palabras:    # par es una tupla
    print(par[1])

for clave, valor in palabras.items():
    print(valor)

