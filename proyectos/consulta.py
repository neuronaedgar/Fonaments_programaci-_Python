class consulta:
    
    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, pac):
        if pac is not None:
            self.__paciente = pac

    
    def __init__(self, medico):
        self.__medico = medico
        self.__paciente = None