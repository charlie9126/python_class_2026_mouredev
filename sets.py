### Sets ###


my_set = set()
my_other_set ={}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un Diccionario

my_other_set = {"Carlos", "Diaz", 34}
print(type(my_other_set))

print(len(my_other_set))

#Un set no es una estructura ordenada
# Un set no admite repetidos

my_other_set.add("Carlosdev")
print(my_other_set)
#posibilidad de hacer busquedas
print("Diaz" in my_other_set)
print("Diez" in my_other_set)

my_list = list(my_set)