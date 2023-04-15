#enumerado colores
import enum

class color(enum.Enum):
    rojo = 1
    verde = 2
    azul = 3


item_color = "amarillo"

item_color = color.azul

if item_color == color.azul:
    pass



