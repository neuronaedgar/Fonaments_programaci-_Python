import sys # Modulo para poder pasar parámetros. DRY
#import sys.argv
import funciones as f #f es alias para recortar

""" CREO funciones en un modulo funciones.py
# Definición de una función -DRY
# con las funciones te permite la escalabilidad.
def mostrar_mensaje(nom):
    print(f"Hola, soy {nom} the boss")

def convertir_mensaje_mayusculas(cadena):
        return cadena.upper()

def slice(cadena,inicial,final):
    #if cadena
    if cadena is not None:
        if inicial>=0 and final<=len(cadena):
            return cadena[inicial:final]
    
"""
# __name__ variable del Propiedades del modulo
if __name__ == "__main__":
    nombre = sys.argv[1] # las variables globales viven hasta fin del programa, Variable global.
    #print(f"Hola, soy {nombre} the boss")
    destino = None # nulo.
    f.mostrar_mensaje(nombre)
    print(f.convertir_mensaje_mayusculas(nombre))
    
    #caso ideal
    print("La cadena recortada es:",f.slice(nombre,1,3))

    # caso anomalo
    print("La cadena recortada es:",f.slice(None,1,8)) # cuando una función no devuelve nada, devuelve None

else:
    print("No soy principal")