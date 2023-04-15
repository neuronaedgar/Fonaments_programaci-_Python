def sumar(x ,y,):
    return x+y

print(sumar(10,3))


# funcion lambda -> paradigma funcional de Python
sumar2 = lambda x , y : x + y
print(sumar2(10,4))

print(0.0000000000000000000001)
#sumar2 -> es una variable

sumar_doble = lambda x , y : sumar(x,y) * 2
multiplicar = lambda x , y : x * y

print(f"Sumar doble: {sumar_doble(2,8)}")