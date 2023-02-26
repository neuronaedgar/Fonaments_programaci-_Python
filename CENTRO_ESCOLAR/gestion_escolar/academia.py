#seleccionar el tipo de estructura para soportar un alumno
def __crear_alumno(dni:str, nombre:str, apellido:str) -> tuple:
    ''' funcion que recibe un dni, un nombre y un apellido 
        y crea un elemento alumno '''
    return (dni, nombre, apellido)  

def crear_alumnos() -> list:
    '''funcion que crear unos alumnos con dni, nombre y apellido para luego ser matriculados'''
    l_alumnos = []
    l_alumnos.append(__crear_alumno('38512111', 'Juan', 'Perez'))
    l_alumnos.append(__crear_alumno('38512222', 'Alicia', 'Bartomeu'))
    l_alumnos.append(__crear_alumno('38512333', 'Victor', 'Sanchez'))
    l_alumnos.append(__crear_alumno('38512444', 'Marta', 'Navarro'))
    l_alumnos.append(__crear_alumno('38512555', 'Daniela', 'Lopez'))

    return l_alumnos

def __matricular_alumno(t_alumno: tuple) -> tuple:
    '''funcion que recibe los datos basicos de alumno y devuelve los datos ampliados con curso y asignaturas'''
    #return (t_alumno[0],t_alumno[1],t_alumno[2], 1, {'mates', 'literatura', 'filosofia'})
    dni, nombre, apellido = t_alumno
    return (dni, nombre, apellido, 1, {'mates', 'literatura', 'filosofia'})

def matricular_alumnos(l_alumnos: list) -> list:
    '''funcion que devuelve los alumnos con las nuevas informaciones del centro escolar'''
    l_matriculados =  []
    for alumno in l_alumnos:
        info_alumno = __matricular_alumno(alumno) 
        l_matriculados.append(info_alumno)
    else:
        return l_matriculados


def listar_alumnos(l_alumnos: list) -> list:
    '''funcion que devuelve los datos de alumnos dni y curso '''
    info_requerida = []
    for alumno in l_alumnos:
        dni, _, _, curso, *_ = alumno
        print("CURSO:", curso)
        info_requerida.append((dni, curso))
    else:
        return info_requerida



def __examinar_alumno_con_calificacion(s_asig: set) -> float:
    import random as R
    asignatura = R.choice(list(s_asig))
    return round(R.uniform(0.0, 10.0),2) 

def examinar_alumnos_con_calificacion(l_alumnos: list) -> list:
    l_calificaciones = list()
    for alumno in l_alumnos:
        resultado = __examinar_alumno_con_calificacion(alumno[-1])
        l_calificaciones.append((alumno[0],'?',resultado))
    else:
        return l_calificaciones

def __examinar_alumno(s_asig: set) -> bool:
    import random as R
    asignatura = R.choice(list(s_asig))
    print("Asignatura a examinar:", asignatura)
    return R.choice([True, False]) #hard coded

def examinar_alumnos(l_alumnos: list) -> bool:
    for alumno in l_alumnos:
        resultado_accion = __examinar_alumno(alumno[-1])
        if resultado_accion == False:
            break
    else:
        return True
    return False

def buscar_detalle_alumno(id_alumno: str, l_alumnos: list) -> tuple:
    alumno_buscado = None
    for alumno in l_alumnos:
        if alumno[0] == id_alumno:
            alumno_buscado = alumno
            break
    
    return alumno_buscado


