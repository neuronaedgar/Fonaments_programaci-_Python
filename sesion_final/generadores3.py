lista = list(range(50))

# comprengencion list

lista2 = [i + 2 for i in lista]

# es un generator , no es un comprongention
# es una lista con generador optimizada en memoria.
# un generador es un iterador.
gen1 = (i + 2 for i in lista)
print(type(gen1))  # <class 'generator'>

print(gen1.__next__())

def devolver_data():
    for item in lista2:
        if item > 25:
            break
        else:
            yield item


