from paciente import paciente

class sala_espera ():  

    #lista_pacientes = []   # cada objeto sala_espera tiene un listado de paciente diferente, no es public.
    
    @property       # solo permites leer el atributo __dni
    def lista_pacientes(self):
        return self.__lista_pacientes
   

    def put_paciente(self,paciente: paciente):
        if paciente is not None:
            self.__lista_pacientes.append(paciente)

    def delete_paciente(self, dni:str):
        paciente = self.__buscar_paciente(dni)
        self.__lista_pacientes = [paciente for paciente in self.__lista_pacientes if paciente.dni != dni] # comprehecion list mucho mas eficiente que for.
        return paciente
    
    def eliminar_paciente(self, dni:str):
        paciente = self.__buscar_paciente(dni)
        self.__lista_pacientes = [paciente for paciente in self.__lista_pacientes if paciente.dni != dni]
        return paciente
'''
    def __buscar_paciente(self, dni):
        return list(filter(lambda pac : pac.dni == dni, self.__lista_pacientes))
'''
    def __buscar_paciente(self, dni: str) -> paciente:
        data = list(filter(lambda pac : pac.dni == dni, self.__lista_pacientes)) 
        return data[0]

    # atributos de la instancia / objeto
    # constructor de la clase.
    #def __init__(self):
    #    self.__lista_pacientes = []        # atributo privado y vacio 
    
    def __init__(self):
        self.__lista_pacientes = list()
