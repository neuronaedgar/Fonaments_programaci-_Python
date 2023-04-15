from persona import persona

class medico(persona):
    data = 1
    @property
    def numero_colegiado(self):
        return self.__colegiado
    
    @property
    def especialidad(self):
        return self.__especialidad
    
    @especialidad.setter
    def especialidad(self, nueva_espec):
        self.__especialiad = nueva_espec

    
    #constructor
    def __init__(self, dni, nombre, apellido, edad, colegiado, especialidad):
        super().__init__(dni, nombre, apellido, edad)
        self.__colegiado = colegiado
        self.__especialiad = especialidad

    @classmethod
    def crear(cls, dni, nombre, apellido, edad, colegiado, especialidad):
        return cls(dni, nombre, apellido, edad, colegiado, especialidad)
  