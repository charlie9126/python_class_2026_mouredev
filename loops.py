### loops ###

#while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional, pero se puede colocar en python
    print("Mi condicion es mayor o igual a 10")

print("la ejecucion Continúa")


#For 
my_list = [35, 24, 45, 25, 38, 38, 17]

for element in my_list:
    print(element)


my_tuple = (34, 1.70, "Carlos", "Diaz", "Carlos")
for element in my_tuple:
    print(element)

my_set ={"Carlos", 91, "Andres"}
for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Carlos",
    "Apellido":"Diaz",
    "Edad":34,
    "Lenguajes":{"Python", "Js", "C#", "Swift"}
}
for element in my_dict:
    print(element)


for element in list(my_dict.values()):
    print(element)
else:
    print("El bucle for del diccionario ha finalizado")


for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for del diccionario ha finalizado")