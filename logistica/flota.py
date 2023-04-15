"""
Esta clase se responsabiliza de ....
"""
from typing import List

from camion_motor import camion_motor
class flota:
    
    def __init__(self) -> None:
        self.__camiones = list()

    def add(self, camion):
        self.__camiones.append(camion)

    def llenar_camiones(self, items):
        for camion in self.__camiones:
            for pos, item in enumerate(items):
                camion.cargar(pos, item)

    def vaciar_camiones(self, items):
        pass

    def iniciar_marcha(self, o_trabajo):
        for camion in self.__camiones:
            camion.arrancar()


    def __getitem__(self, index):
        return self.__camiones[index]

    def __setitem__(self, index, camion):
        """Metodo que sirve para modificar, no crear"""
        self.__camiones[index] = camion
    