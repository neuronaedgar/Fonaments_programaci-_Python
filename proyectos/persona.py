import datetime

class persona:

    @property #solo permites leer el atributo __dni
    def dni(self):
        return self.__dni
    
    @property #solo permites leer el atributo __dni
    def nombre(self):
        return self.__nombre
    
    @property #solo permites leer el atributo __dni
    def apellido(self):
        return self.__apellido
    
    @property #solo permites leer el atributo __dni
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > self.__edad:
            self.__edad = nueva_edad

    #constructor
    def __init__(self, dni, nombre, apellido, edad):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad   

    
        #API - comportamiento
    def pedir_cita(self) -> datetime:
        return  datetime.datetime.now()
    
    def  __str__(self) -> str:
        return f"{self.__dni} - {self.__nombre} {self.__apellido}"
    
    def __eq__(self, p) -> bool:
        return self.__edad == p.edad