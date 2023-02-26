

from gestion_escolar.academia import (crear_alumnos,
                                        matricular_alumnos, 
                                            listar_alumnos, 
                                                examinar_alumnos,
                                                    examinar_alumnos_con_calificacion,
                                                        buscar_detalle_alumno)

from gestion_escolar.gestion_premios.premios import obtener_premiados

import ficheros as fic

"""
1- crear alumnos ok revisable
2.- matricular alumnos ok revisable
3.- examinar alumnos
4.- Obtener calificaciones
5.- Reparto premios y diplomas: a los dos alumnos con mejores calificaciones
6.- guardar los datos de los ganadores en un fichero.
"""


if __name__ == "__main__":
    alumnos = crear_alumnos()
    print(f"Hemos creado {len(alumnos)} alumnos")
    #listar_alumnos(alumnos)
    alumnos_matriculados = matricular_alumnos(alumnos)
    #print(listar_alumnos(alumnos_matriculados))
    
    resultado_examenes = examinar_alumnos(alumnos_matriculados)
    if resultado_examenes:
        print("El proceso de examenes ha ido correctamente")
    else:
        print("El proceso de examenes NO ha ido correctamente. Contactar con el tutor")
    
    alumnos_calificados = examinar_alumnos_con_calificacion(alumnos_matriculados)
    print(alumnos_calificados)

# TODO Crear un sistema ordenado de alumnos con mejores calificaciones
    primer_premio, segundo_premio = obtener_premiados(alumnos_matriculados) # unboxing de la tupla
    print(f"el primer premiado es: {primer_premio} y el segundo es {segundo_premio}")
    #Alternativa
    print("el primer premiado es: {} y el segundo es {}".format(primer_premio, segundo_premio))

    fic.guardar_datos((str)(alumnos_matriculados))