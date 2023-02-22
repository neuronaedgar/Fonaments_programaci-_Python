# función que persiste los datos en un fichero
def guardar_datos(data):
    with open('premiados.txt','w') as f:
        f.write(data)
