from vehiculo_motor import vehiculo_motor
from vehiculo_electrico import vehiculo_electrico
from vehiculo import vehiculo

class camion(vehiculo):
    def __init__(self) -> None:
        pass

    def cargar():
        pass

    def descargar():
        pass

class camion_hibrido(vehiculo_motor, vehiculo_electrico):  # herencia multiple.
    pass

class camion_combustion(vehiculo_motor):  # herencia.
    pass

class camion_electrico(vehiculo_electrico):  # herencia.
    pass


