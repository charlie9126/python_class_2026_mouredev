### Functions ###

def my_function ():
    print("Esto es una funcion")

my_function()

def sum_two_values (firs_number, second_number):
    print(firs_number + second_number)

sum_two_values(2,3)

def sum_two_values_with_return (firs_number, second_number):
    return firs_number + second_number

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Carlos", "Diaz")

##Con el * antes del la variable se puede colocar varias cademas de textos
##Numero de casos dinamico
## funcion con parametros arbitrarios
def print_texts(*text):
    print(text)

print_texts("Hola", "python", "CarlosDev")

