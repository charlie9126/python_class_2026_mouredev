### CLASSES ###

### No va en snake_case lleva CamelCase
class Person:
    ##constructor de clase
    def __init__(self, name, surname):
        ##Propiedades de la clase
        self.name = name
        self.surname = surname
    

my_person = Person("Carlos", "Diaz")
print(f"{my_person.name} {my_person.surname}")

class Person2:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} está Caminando")

my_person2 = Person2("Victoria", "brausi", "vicsales")
print(my_person2.full_name)
print(type(my_person2))
my_person2.walk()

