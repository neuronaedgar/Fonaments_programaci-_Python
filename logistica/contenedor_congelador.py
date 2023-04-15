from congelador import congelador
from contenedor import contenedor

class contenedor_congelador(contenedor, congelador):
    
    def __init__(self, capacidad) -> None:
        super().__init__(capacidad)
        