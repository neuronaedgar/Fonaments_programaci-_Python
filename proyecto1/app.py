print("Hola desde Visual Studio")

'''
movemos datos
uso de variables
que nos permiten almacenar valores
'''

#NOTACION PYTHON: SNAKE
#alumno
nombre = "Edgar" #cadena o literal
apellido = "Navarro" #cadena o literal
segundo_apellido = "Andres" #cadena o literal

print(nombre, apellido, segundo_apellido) #Ricardo*Jaume

nota_parcial = 5.5 #float
numero_intentos = 2 #int

print(type(nota_parcial))
print(type(numero_intentos))
print(type(nombre))

tiene_hijos = True
print(type(tiene_hijos))
esta_casado = False

tiene_hijos_y_esta_casado = tiene_hijos and esta_casado
print(type(tiene_hijos_y_esta_casado))
print(tiene_hijos_y_esta_casado)

saludo = f"Hola, me llamo {nombre} {apellido}"
print(saludo)

numero_caracteres_saludo = len(saludo)
print(f"El num. de caracteres de saludo es {numero_caracteres_saludo}")

#primer elemento de la variable saludo
print(saludo[0])
#último elemento de la variable saludo (leng. tradicional)
print(saludo[len(saludo) - 1])

#último elemento de la variable saludo (leng. python)
print(saludo[-1])

tramo_1 = saludo[:7] #slice / slicing
print(tramo_1)

tramo_2 = saludo[10:] #slice / slicing
print(tramo_2)

#nombre_completo = nombre + " " + apellido
nombre_completo = f"{nombre} {apellido} xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
print(f"Nombre completo:{nombre_completo}")

nombre_2 = nombre_completo[0:nombre_completo.index(' ')]
apellido_2 = nombre_completo[nombre_completo.index(' ') + 1:]

print("Nombre", nombre_2, sep=":")
print("Apellido", apellido_2, sep=":")

"""
si la longitud de mi nombre completo es mayor a 35 
entonces separame el nombre complet en nombre y apellido
"""
print(len(nombre_completo))
if len(nombre_completo) > 35:
    nombre_2 = nombre_completo[0:nombre_completo.index(' ')]
    apellido_2 = nombre_completo[nombre_completo.index(' ') + 1:]
    print(nombre_2, apellido_2, sep="-")
else:
    print("NO hay operacion de slicing")    






















