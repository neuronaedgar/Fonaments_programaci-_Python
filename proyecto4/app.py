from ficheros import guarda_items, devolver_items

items = range(2,10,4)

for item in items:
    print (item)

# comprehension list
nuevos_items = [item *5 for item in items]   
print(nuevos_items)  # [10, 30]


# comprehension set
nuevos_items_set ={item *3 for item in items}
print(nuevos_items_set)  # {18, 6}


# comprehension dict
nuevos_items_dict ={item:item * 2 for item in items}
print(nuevos_items_dict)  # {2: 4, 6: 12}

guarda_items("kk.txt",nuevos_items_dict)    # *.pckl -> binario entrado con pickle
guarda_items("kk.txt",nuevos_items_set)

try:
    lista = devolver_items("kk2.txt")
except Exception as ex:
    print(ex)
else:
    print(lista)

lista = devolver_items("kk.txt")
print(lista)

# recuperar
