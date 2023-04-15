# programacion funcional
# match patter
# el match es un switch sin serlo

import sys

print(sys.platform)

match sys.platform:
    case "linux":
        print("estas en linux")
    case "win32":
        print("estas Windows")
    case "darwin":
        print("estas en linux")
    case _: # else
        raise NotimplementedError(f"esta plataforma {sys.platform} no esta permitida")
    

