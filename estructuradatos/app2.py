#edatos
#set

# conjuntos {}
# tupla ()
# listas []

conjunto1 = {1,2,3,2,1,3,2,1,2,3,1,2,3,1,2,3}
print(conjunto1)
print(len(conjunto1))

lista = range(100) 
print(type(lista)) # <class 'range'>
suma = 0  # en python no puedes emplear una variable sin inicializarla.
for i in range(5): # cinco vueltas
    suma = suma + 1
    print(i)

print(suma)

lista = list(range(100))  # cast de range a una lista
print(type(lista)) # <class 'list'>

conjunto_a = set(lista)
print(len(conjunto_a))

conjunto_b= {1,4,7,10,21,45}

conjunto_c = conjunto_a.difference(conjunto_b)
print(len(conjunto_c))
print(conjunto_c)
l = ()
for i in range(10):
    l=list(conjunto_c)
    print(l[i])

for num in list(conjunto_c)[:5]:
    print(num)


conjunto_d = conjunto_c.intersection(conjunto_b)
print(len(conjunto_d))  # 0
print(conjunto_d)

conjunto_e = conjunto_b.union(conjunto_c)
print(len(conjunto_e))  # 100 recontruyo el conjunto


