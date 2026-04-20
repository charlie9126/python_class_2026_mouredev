### Exceptions ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    # Se Ejecuta si existe una excepción
    print("Se ha producido un error")
else:
    # Se ejecuta si no produce una excepción
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")

#Captura que error es 

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError:
    # Se Ejecuta si existe una excepción
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as execption:
    print(execption)
