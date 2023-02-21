import calculadora as calc
import sys

def pedir_sumandos():
    # input() - funcion built-in de python
    x = int(input("entrar primer numero:"))   # casting de caracter a integer.
    y = int(input("entrar segundo numero:"))

    # Estructura de datos tupla (1,2,3,4,5) agrupacion de numeros
    return (x, y)  # las Tuplas no se pueden modificar.

def pedir_operacion():  
    oper = input("Que operacion quieres realizar (+,-,/,*)?:")
        #if (oper == "+" or oper == "-" or oper == "/" or oper == "*"):
    return oper

def mostrar_mensaje(mensaje):
    print(mensaje)

if __name__ == "__main__":

    #primero = sys.argv[1]
    #segundo = sys.argv[2]

    tupla_sumandos = pedir_sumandos()
    operacion = pedir_operacion()
    if operacion == "+":
        resultado = calc.suma(tupla_sumandos[0],tupla_sumandos[1])
    elif operacion == "-":
        resultado = calc.resta(tupla_sumandos[0],tupla_sumandos[1])
    elif operacion == "*":
        resultado = calc.multiplicacion(tupla_sumandos[0],tupla_sumandos[1])
    elif operacion == "/":
        resultado = calc.division(tupla_sumandos[0],tupla_sumandos[1])
    else:
        print("Operacion no permitida")
        sys.exit(1)


    mostrar_mensaje(f"El resultado de la operación es {resultado}")
"""
    print("La Suma es: ",calc.suma(primero,segundo))
    print("La Resta es: ",calc.resta(primero,segundo))
    print("La Multiplicacion es: ",calc.multiplicacion(primero,segundo))
    print("La División es: ",calc.division(primero,segundo))5
"""