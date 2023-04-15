import logging

def my_funcion(a ,b , data, i) -> int:
    if a is not None and b is not None:
        print(data[i]) # accedo a mi dicceonario por una clave que no existe. Error KeyError: 3

datos = dict()

datos[1] = "Datos1"
print(datos[1])

info = dict([(2,"datos2")])
datos.update(info)

print(datos)

# control de excepciones

try: # Pruebo la función y controlo el error.
    my_funcion(1, 8, datos, 2)
    mii_funcion(1, 8, datos, 2)
    my_funcion(1, 8, datos, 3)

except KeyError: 
    print("Ha habido un error con el acceso a la clave")

except NameError:
    print("Ha habido un problema con el nombre de la alguna funcion")

except: # solo se ejecuta, Si hay error y es generico.
    print("Ha habido un problema general")

else: # solo se ejecuta, si no ha habido un error
    print("Todos ha ido bien")

finally: # El finally siempre se ejecuta, si ha habido o no error.
    print("Fin del proceso")

logging.basicConfig(level=logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')









