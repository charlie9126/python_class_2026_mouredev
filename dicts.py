### DICTIONARIES ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Carlos", "Apellido":"Diaz", "Edad":35}
my_dict = {
    "Nombre":"Carlos",
    "Apellido":"Diaz",
    "Edad":34,
    "Lenguajes":{"Python", "Js", "C#", "Swift"}
}
print(my_other_dict)
print(my_dict)

my_dict["Nombre"] = "Andres"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Diaz"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", "Edad", "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

