#clase datafono
class datafono:
    entidad = "ING"

    def conectar(self) -> tuple:
        return (f"Conectando con {self.entidad}...", True)
    
    def realizar_cargo(self, cantidad: float) -> bool:
        return True

    def imprimir_copia(self) -> str:
        return "Copia para el cliente"

def crear_datafono() -> datafono:
    return datafono()    

#programa pueda usar el objeto datafono
if __name__ == "__main__":
    datafono_tienda = crear_datafono()

    if datafono_tienda is not None and  isinstance(datafono_tienda, datafono):
        print(f"Datafono de la entidad {datafono_tienda.entidad} creado correctamente")
        resultado_conexion = datafono_tienda.conectar()
        if resultado_conexion[-1] == True:
            print(resultado_conexion[0])
            if datafono_tienda.realizar_cargo(123.90):
                print(datafono_tienda.imprimir_copia())

                