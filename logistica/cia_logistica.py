from collections import namedtuple
from flota import flota

class cia_logistica:

    def __init__(self):
        self.__flota = flota()
    
    def anyadir_vehiculo(self, vehiculo):
        self.__flota.add(vehiculo)

    def llenar_camiones(self, mercancia):
        self.__flota.llenar_camiones(mercancia)

    def __crear_orden_trabajo(self, origen, destino, cliente):
        import datetime

        f_sistema = datetime.datetime.today()
        orden_trabajo = namedtuple("orden_trabajo", ['origen', 'destino','cliente', 'fecha'])
        orden = orden_trabajo(origen=origen,destino=destino,cliente=cliente, 
                                            fecha=f"{f_sistema.day}-{f_sistema.month}-{f_sistema.year}")

        return orden

    def iniciar_marcha(self, origen, destino, cliente):
        orden_trabajo = self.__crear_orden_trabajo(origen=origen, destino=destino, cliente=cliente)
        self.__flota.iniciar_marcha(orden_trabajo)

    

    

