from vehiculo_motor import vehiculo_motor
from contenedor import contenedor

class camion_motor(vehiculo_motor):
    
    @property
    def capacidad(self):
        return self.__carga.capacidad
    
    def __init__(self, capacidad) -> None:
        self.__carga = contenedor(capacidad)
        

    def cargar(self, pos, item):
        if pos < self.capacidad:
            self.__carga[pos] = item

    def descargar(self, pos) -> any:
        if pos < self.capacidad:
            return self.__carga[pos]
