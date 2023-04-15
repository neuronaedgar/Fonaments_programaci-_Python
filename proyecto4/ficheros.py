import pickle

f = None
# las funciones deberian ser atomicas
def guarda_items(nombre_fichero: str, items:list):
    if items is None:
         return
    f = None
    try:    
        f = open(f"data/{nombre_fichero}", 'ab')  # En escrituras no hace falta que exista el fichero, los crea. En acceso lectura es obligatorio que exista.
        pickle.dump(items,f)
        
    except FileNotFoundError:
        print(f"No se encontro el fichero {nombre_fichero}")
    
    except:
            print("Error general")
    
    finally:
         if f is not None:
              f.close() 

def devolver_items(nombre_fichero: str) -> list:    # es mejor poner -> any pues puede devolver otra cosa.
    f = None
    lista = None
    try:    
        f = open(f"data/{nombre_fichero}", 'rb')  # En acceso de lectura es obligatorio que exista el fichero.
        lista = pickle.load(f)
        
    except FileNotFoundError as ex:
        #print(f"No se encontro el fichero {nombre_fichero}")
        #raise Exception("No se ha encontrado fichero")
        raise ex

    except ValueError as ve:
        raise ve
    finally:
        if f is not None:
              f.close()
        return lista 