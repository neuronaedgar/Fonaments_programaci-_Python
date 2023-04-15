from paciente import paciente
from sala_espera import sala_espera
from asignacion_exception import asignacion_exception

class centro_medico:
    def __init__(self, medicos = None, salas_esperas = None):
        self.__pacientes = None
        self.__medicos = medicos
        self.__salas_espera = salas_esperas

    def listar_pacientes(self, l_pacientes:list):
        for paciente in l_pacientes:
            print(paciente)      # printa la direccion de memoria <paciente.paciente object at 0x7ff17695fdf0>

    def listar_pacientes(self, l_pacientes:list):
        for paciente in l_pacientes:
            print(paciente) 

    def pedir_visita(self, *pacientes):
        for paciente in pacientes:
            paciente.pedir_cita()

    def cargar_pacientes(self, f_pacientes) -> list:
        l_pacientes = None  
        with open('data/pacientes.txt','r') as f:
            l_pacientes = [paciente(linea.strip().split(',')[0],
                                        linea.strip().split(',')[1],
                                            linea.strip().split(',')[2],
                                                linea.strip().split(',')[3],
                                                    linea.strip().split(',')[4]) for linea in f.readlines()]
        return l_pacientes

    def llenar_sala_espera(self, l_pacientes, s_espera:sala_espera):
        for paciente in l_pacientes:
            s_espera.anyadir_paciente(paciente)


    def asignar_medico(self, l_pacientes: list, medico):
        self.__pacientes = [paciente(p.dni, p.nombre, 
                            p.apellido, p.edad,
                                p.cip, medico) for p in l_pacientes]

    def asignar_medico_v2(self, l_pacientes: list, medico):
        self.__pacientes = list(map(lambda p:paciente(p.dni, p.nombre, 
                                        p.apellido, p.edad,
                                            p.cip, medico), l_pacientes))
    @staticmethod
    def cerrar_centro(hora):
        if hora > 22:
            print("Cerrando centro...")