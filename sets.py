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

my_list = list(my_other_set)
print(my_list)
print(my_list[0])
my_set ={"Carlos", 91, "Andres"}
print(my_set)

my_new_set =  my_set.union(my_other_set)
print(my_new_set)

print(type(my_new_set))