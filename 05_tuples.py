### Tuple ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (34, 1.70, "Carlos", "Diaz", "Carlos")
my_other_tuple = (31, 12, 51)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

print(my_tuple.count("Carlos"))
print(my_tuple.index("Carlos"))



"""
La tupla es inmutable
"""
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# SLICE OF TUPLE

print(my_sum_tuple[3:6])