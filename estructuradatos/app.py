
def cambiar_tupla_lista(tup: tuple) -> list:
    if tup is not None:
        lista = list() # lista vacia y variable local.
        for num in tup:
            lista.append(num)
        return lista
    else:
        return None

def crear_items(a: int, b: int, c: int) -> list: #type hint -> tipado de los elemento.
    lista = []    #Lista vacia y variable local.
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return lista

def append_elemento(elem: int, l_item: list) -> list:   # las listas se pasan por "referencia" y los int por valor "copia"
    if l_item is not None and elem is not None:
        l_item.append(elem)
        return l_item

def insert_elemento(elem, pos: int, l_item:list) -> list:
    if l_item is not None and elem is not None and pos is not None:
        l_item.insert(pos, elem)
        return l_item


def mostrar_items(l_items:list):
    for item in l_items:
        print("Los item son", item, sep=":")

def order_list(l_item:list) -> list:
    if l_item is not None:
        return l_item.sort()
        #return sorted(l_item) # no se porque no funciona


if __name__ ==   "__main__": # bloque de codigo del programa principal
    pass #palabra reservada para permitir pasar un bloque sin error "IndentationError".
    #lista_item = crear_items(6,8,3)  # variable lista_item es global
    #mostrar_items(lista_item)
    
    tupla_mod = ("A","B","C", 6) # tupla () Lista []
    lista_item2 = cambiar_tupla_lista(tupla_mod)
    #lista_item2 = None
    if lista_item2 is not None:
        mostrar_items(lista_item2)
    else:
        print("Sin Datos a mostrar porque la tupla esta vacia")

    subrayado = ["________________________"]
    mostrar_items(subrayado)   
    lista_item3 = ["A","B","C","D","E"]  # tupla () Lista []

    insert_elemento("A", 2,lista_item3)
    mostrar_items(lista_item3)

    subrayado = ["________________________"]
    mostrar_items(subrayado)   

    append_elemento("f",lista_item3)
    mostrar_items(lista_item3)

    mostrar_items(["________________________"])   
    lista_item4 = [1,5,123,3,2,1]
    order_list(lista_item4)
    mostrar_items(lista_item4)

    tupla = (1,4,7,2,3,7,9)
    tupla_ordenada = sorted(tupla)
    print(tupla_ordenada)

    # conjuntos (SET) Estructura de datos NO ORDENADA, no garantiza el orden y NO permite DUPLICADOS
    l = list()
    conjunto = set() # conjunto vacio. Es modificable
    conjunto.add(1)
    conjunto.add(2)
    conjunto.add(3)
    print(conjunto)

    conjunto2 = set(lista_item3)
    print(conjunto2)

