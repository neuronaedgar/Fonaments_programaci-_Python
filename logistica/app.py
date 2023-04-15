"""
Programa principal de logistoca que usa las entidades....
"""

from cia_logistica import cia_logistica
from flota import flota
from camion_electrico import camion_electrico
from contenedor_congelador import contenedor_congelador
from camion_motor import camion_motor
from datetime import datetime
"""
Punto de entrada de ....
"""

from collections import namedtuple

if __name__ == "__main__":

    cia = cia_logistica()
    cia.anyadir_vehiculo(camion_motor(capacidad=10))
    #flota.add(camion_electrico(5))

    mercancia = [contenedor_congelador(capacidad=5),contenedor_congelador(capacidad=5)]
    cia.llenar_camiones(mercancia)
    cia.iniciar_marcha("Alemania","Barcelona","Zara")


    
    

    