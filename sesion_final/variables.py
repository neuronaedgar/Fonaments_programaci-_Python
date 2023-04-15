a = 1  # variable global las varriables antes de usarlas debes definirlas.

if a > 7:
    x = 0 # Variable local al if
else:
    y = 0 # Variable local al else

def calcular():
    global a    # No es Shadow, cambia variable global
    a = 12 # Variable local shadowing (no modifica a la variable global)
    print(a + 1)

calcular()
print(a)

