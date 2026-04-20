### Conditionals ###

my_condition = True

if my_condition:
    print("Se ejecuta la condicion del if")

print("La ejecucion continua")

my_condition = 5/5

if my_condition == 10:
    print("Se cumple el sefundo if")

print("La ejecucion continua")

if my_condition > 10 and my_condition < 20:
    print("Es Mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")


my_string ="Mi cadena de texto"

if my_string:
    print("Mi Cadena de texto no es vacia")