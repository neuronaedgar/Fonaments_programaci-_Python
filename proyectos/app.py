from typing import List  # importo una lista objeto

from paciente import paciente
#import paciente as pac   # se puede importar de las dos formas from paciente import paciente
from sala_espera import sala_espera
from paciente import paciente
from consulta import consulta
from medico import medico
from centro_medico import centro_medico
from asignacion_exception import asignacion_exception


'''
paciente_carlos = paciente()
paciente_carlos.nombre = "Carlitos"
paciente_carlos.edad = 99
paciete_ena = paciente()
paciete_ena.nombre = "Edgar"
paciete_ena.edad = 50
sala_espera = [paciente_carlos,paciente_pedro,paciente_ena]
'''




if __name__ == '__main__':

    #medico_familia = medico('50.999.999', 'Dra. Laura', 'Gomez', 26, '23.999', 'Medico familia')
    #medico_familia = medico('99H', 'Laura', 'Gomez', 26, '234567', 'Medico familia')
    medico_familia = medico.crear('99H', 'Dra. Laura', 'Gomez', 26, '234567', 'Medico familia')
    sala_espera_1 = sala_espera()
    centro = centro_medico([medico_familia], [sala_espera_1])

    centro.cargar_pacientes('pacientes')
    #TODO: resolver el uso internmo de la signacion de medico a traves constructor
    try:
        centro.asignar_medico_v2(medico_familia)
    except asignacion_exception as aex:
        print(aex)
    except:
        print("Error general")

    #centro.listar_pacientes()

    #consulta_cap = consulta(medico_familia) #necesario pasarle un medico

    centro_medico.cerrar_centro(23)

'''
    sala_espera_1 = sala_espera()
    centro = centro_medico([medico_familia],[sala_espera_1])
    consulta_cap
    #pacientes = asignar_medico(pacientes, medico_familia)
    #pacientes = asignar_medico_v2(l_pacientes, medico_familia)

    listar_pacientes(pacientes)
    pedir_visita(*pacientes)


    # instanciar la clase paciente
    paciente_carlos = paciente("46763434","Carlos", "Perez", 34,'CIP_111')
    #paciente_ena = paciente("46741593G","Edgar", "Navarro", 50,'CIP_123')
    paciente_pedro = paciente("46111999","Pedro", "Piqueras", 99,'CIP_333')

    paciente_carlos.edad = 35 # setter

    paco = paciente('66H', 'Paco', 'Lobato', 44, 'CIP_123')
    print(paco.apellido)

    #instanciar la clase sala_espera
    cap_del_pueblo = sala_espera()
    cap_del_pueblo.put_paciente(paciente_carlos)
    cap_del_pueblo.put_paciente(paciente("46741593G","Edgar", "Navarro", 50,'CIP_999'))
    cap_del_pueblo.put_paciente(paciente_pedro)


    #instanciar consulta
    consulta_cap = consulta(medico('99H', 'Laura', 'Gomez', 26, '234567', 'Medico familia')) #necesario pasarle un medico
    

    #listar_pacientes(cap_del_pueblo.pacientes)

    #el paciente ha pasado a visita
    paciente_11h = cap_del_pueblo.eliminar_paciente('11H')

    #workflow de visita/consulta
    consulta_cap.paciente = paciente_11h


    #listar_pacientes(cap_del_pueblo.pacientes)


    #listar_pacientes(cap_del_pueblo.lista_pacientes)
    #cap_del_pueblo.delete_paciente("46741593G")
    #listar_pacientes(cap_del_pueblo.lista_pacientes)
'''
'''
    for paciente in cap_del_pueblo:
        print(f'Nombre: {paciente.nombre} {paciente.apellido} su edad: {paciente.edad}')


    for paciente in sala_espera:
        print(f'Nombre: {paciente.nombre} {paciente.apellido} su edad: {paciente.edad}')
        print(paciente.dni)

'''
