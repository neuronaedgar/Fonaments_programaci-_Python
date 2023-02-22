"""
    1.- ordenar alumnos por calificacion de forma descendientes.
    2.- obtener los dos primeros
    3.- devolver estos elementos
"""
def __buscar_alumno_por_calificacion(calif: float, l_alumnos: list) -> str:
    #pass # --> para dejar la funcion sin codificar.
    indice = 0
    encontrado = False
    while indice < len(l_alumnos) and not encontrado:
        if l_alumnos[indice][-1]== calif:
            encontrado = True
        indice = indice +1
    else:
           print("Lo he encontrado")
           return l_alumnos[indice-1][0]

def obtener_premiados(l_alumnos:list) -> tuple:
    """obtener de todos los alumnos del centro escolar, los dos con mejor nota"""
    if l_alumnos is not None and len(l_alumnos) > 0:
        #l_alumnos será una lista de tuplas.
        calificaciones = list()
        for alumno in l_alumnos:
            calificaciones.append(alumno[-1])
        else:   # Si finaliza correctamente el for, se va al else.
            calificaciones.sort(reverse=True)
            mejor_calificacion, segunda_mejor_calificacion, *_ = calificaciones
            id_alumno_primer_premio = __buscar_alumno_por_calificacion(mejor_calificacion,l_alumnos)
            id_alumno_segundo_premio = __buscar_alumno_por_calificacion(segunda_mejor_calificacion,l_alumnos)
            return (id_alumno_primer_premio,id_alumno_segundo_premio)
        
def obtener_premiados_mejorado(l_alumnos:list) -> tuple:
    if l_alumnos is not None and len(l_alumnos) > 0:
        l_alumnos.sort(key=lambda al: al[-1], reverse=True)
        return (l_alumnos[0],l_alumnos[1])

