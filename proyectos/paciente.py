from persona import persona

class paciente(persona):
    
    #atributos de clase
    comunidad_autonoma='CA'

    #atributos de instancia / objeto

    @property
    def historia_clicnica(self):
        return self.__historia_clinica
    
    @property
    def cip(self):
        return self.__cip
    
    @property
    def medico_asignado(self):
        return self.__medico_asignado
    
    @medico_asignado.setter
    def medico_asignado(self, medico):
        self.__medico_asignado = medico

    
    # atributos de la instancia / objeto
    # constructor de la clase.
    def __init__(self, dni, nombre, apellido, edad, cip, medico = None):
        super().__init__(dni, nombre, apellido, edad)
        self.__cip = cip                        # proteccion atributo DNI con el __ = propiedades privados
        self.__historia_clinica = None
        self.__medico_asignado = medico

    #sobre-escritura
    def __str__(self) -> str:
        return f"{super().__str__()} {self.__cip} {self.__medico_asignado.dni}"
    
    