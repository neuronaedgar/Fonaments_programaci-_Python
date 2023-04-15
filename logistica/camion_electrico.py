"""
Esta clase se responsabiliza de ....
"""
from vehiculo_electrico import vehiculo_electrico
from contenedor import contenedor

class camion_electrico(vehiculo_electrico):
    
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



