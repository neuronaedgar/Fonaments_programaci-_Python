"""
Esta clase se responsabiliza de ....
"""
class contenedor:
    
    @property
    def capacidad(self):
        return self.__capacidad
    
    def __init__(self, capacidad) -> None:
        self.__capacidad = capacidad
        self.__items = [None] * self.__capacidad

    def llenar(self):
        pass

    def vaciar(self):
        pass

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, camion):
        """Metodo que sirve para modificar, no crear"""
        self.__items[index] = camion

