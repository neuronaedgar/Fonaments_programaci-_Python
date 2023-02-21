# Definición de una función - DRY
# con las funciones te permite la escalabilidad.

print("Nombre Modulo:",__name__)

def mostrar_mensaje(nom):
    print(f"Hola, soy {nom} the boss")

def convertir_mensaje_mayusculas(cadena):
        return cadena.upper()

def slice(cadena,inicial,final):
    #if cadena
    if cadena is not None:
        if inicial>=0 and final<=len(cadena):
            return cadena[inicial:final]
    